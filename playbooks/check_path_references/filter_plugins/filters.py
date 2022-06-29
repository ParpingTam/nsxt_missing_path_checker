from ansible_mongodb_store.mongodb_store import write_to_mongo, read_from_mongo
import logging

def _reduce_to_groups_with_group_members(group_list, group_paths):
    reduced_group_list = list()
    for group in group_list:
        for expression in group['expression']:
            if expression['resource_type'] == 'PathExpression' and 'groups' in expression['paths'][0]:
                for path in expression['paths']:
                    if not path in group_paths:
                        reduced_group_list.append(group)
                        break
                    else:
                        logging.warning("Group: {} - Path {} found!".format(group['display_name'],path))

    return reduced_group_list

class FilterModule(object):
    def filters(self):
        return {
                'find_broken_group_refs': self.find_broken_group_refs,
                'write_to_mongodb': self.write_to_mongodb,
                'read_from_mongodb': self.read_from_mongodb
                }

    def find_broken_group_refs(self,packed_data):
        (group_data, group_paths) = packed_data
        # First reduce groups to be checked only to those that have a group member expression
        groups_with_group_members = _reduce_to_groups_with_group_members(group_data, group_paths)
        return groups_with_group_members

    def write_to_mongodb(self, packed_data):
        (mongo_dict, data, data_type_key) = packed_data
        return write_to_mongo(mongo_dict, data, data_type_key)


    def read_from_mongodb(self, packed_data):
        (mongo_dict, data_type_key) = packed_data
        return read_from_mongo(mongo_dict, data_type_key)