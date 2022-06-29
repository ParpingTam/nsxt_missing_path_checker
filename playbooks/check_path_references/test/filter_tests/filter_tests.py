#!/usr/bin/python
'''
This must be called from playbook level for the pythonpath and mongo files to
be right.
'''
import yaml
from filter_plugins.filters import FilterModule
filterObject = FilterModule()
# REad in the basic mongodb settings from ../../vars/mongodb_settings.yml
with open('../../vars/mongodb_settings.yml') as file:
    try:
        mongo_connection = yaml.safe_load(file)['mongo_connection']
        print(mongo_connection)
    except yaml.YAMLError as exc:
        print(exc)
filterObj = FilterModule()
group_paths = filterObj.read_from_mongodb([mongo_connection,'group_paths'])
group_data = filterObj.read_from_mongodb([mongo_connection,'group_data'])
breakpoint()
return_val = filterObj.find_broken_group_refs([group_data, group_paths])
