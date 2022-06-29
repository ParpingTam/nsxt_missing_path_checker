from ansible_mongodb_store.mongodb_store import write_to_mongo, read_from_mongo



class FilterModule(object):
    def filters(self):
        return {
                'write_to_mongodb': self.write_to_mongodb,
                'read_from_mongodb': self.read_from_mongodb
                }



    def write_to_mongodb(self, packed_data):
        (mongo_dict, data, data_type_key) = packed_data
        return write_to_mongo(mongo_dict, data, data_type_key)


    def read_from_mongodb(self, packed_data):
        (mongo_dict, data_type_key) = packed_data
        return read_from_mongo(mongo_dict, data_type_key)