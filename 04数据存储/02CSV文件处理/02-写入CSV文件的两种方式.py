import csv

headers = ('name','age','height')
# students = [
#     ("张三",18,180),
#     ("李四",19,190),
#     ("王五",20,170)
# ]
students = [
    {"name":"张三","age":18,"height":180},
    {"name":"李四","age":19,"height":190},
    {"name":"王五","age":20,"height":170}
]

# with open("students.csv",'w',encoding='utf-8',newline='') as fp:
#     writer = csv.writer(fp)
#     writer.writerow(headers)
#     writer.writerows(students)


# with open("students.csv",'w',encoding='utf-8',newline='') as fp:
#     writer = csv.DictWriter(fp,headers)
#     # 虽然DictWriter创建的时候有一个headers，但是想要写入数据进去，还是需要调用
#     # writer.writeheader()方法，否则，表头数据写入不进去
#     writer.writeheader()
#     writer.writerows(students)