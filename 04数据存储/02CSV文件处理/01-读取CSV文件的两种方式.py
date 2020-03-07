import csv

# with open("stock.csv",'r',encoding='gbk') as fp:
#     reader = csv.reader(fp)
#     for x in reader:
#         print(x[3])


with open("stock.csv",'r',encoding='gbk') as fp:
    reader = csv.DictReader(fp)
    for x in reader:
        print(x['secShortName'])