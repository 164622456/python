import json

json_str = '[{"name": "三国演义", "price": 18.8}, {"name": "水浒传", "price": 19.9}]'

# print(type(json_str))
# result = json.loads(json_str)
# print(result)
# print(type(result))

with open("books.json",'r',encoding='utf-8') as fp:
    result = json.load(fp)
    print(result)
    print(type(result))



# Python对象->JSON字符串->Python对象