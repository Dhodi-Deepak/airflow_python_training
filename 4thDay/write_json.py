import json
data ={'name':'Deepak','age':30,'city':'Hyderbad','occupation':'Developer','hobbies':['reading','programming','listing music']}
print(data)
with open('write_Json.json', 'w') as f:
    json.dump(data, f)