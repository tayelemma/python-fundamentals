# JSON is commonly used with data API's. 
# Parse JSON into python dictionary

import json


# The key-value pair must be in double quotes for Json file
# json_file = "{'first_name': 'Tom', 'last_name': 'Brady', 'age': 37}" # Runtime error 

# Parse Json into Dict --> loads()
json_file = '{"first_name": "Tom", "last_name": "Brady", "age": 37}'

print(type(json_file)) #str

json_dict = json.loads(json_file)
print("Json to Dict: ", json_dict)

# Dict into Json --> dumps()
dict_file = dict({'firstName': 'Jhon', 'lastName': 'Doe', 'age': 60})

print(type(dict_file))
print(dict_file['firstName'])

dict_json = json.dumps(dict_file)
print("Dict to Json ", dict_json)

