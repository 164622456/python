import json

books = [
    {
        "name": "三国演义",
        "price": 18.8
    },
{
        "name": "水浒传",
        'price': 19.9,
    }
]
print(type(books))

result = json.dumps(books,ensure_ascii=False)
print(result)
print(type(result))

# fp = open("books.json",'w',encoding='utf-8')
# json.dump(books,fp,ensure_ascii=False)
# fp.close()