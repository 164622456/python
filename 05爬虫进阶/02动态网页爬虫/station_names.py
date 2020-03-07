import csv

# with open("stations.txt",'r',encoding='utf-8') as fp:
#     lines = fp.read()
#     result = lines.split("@")
#     stations = []
#     with open("stations.csv",'w',encoding='utf-8') as fp2:
#         writer = csv.DictWriter(fp2,['name','code'])
#         writer.writeheader()
#         for line in result[1:]:
#             infos = line.split("|")
#             station = infos[1]
#             code = infos[2]
#             writer.writerow({'name':station,'code':code})

with open("stations.csv",'r',encoding='utf-8') as fp:
    reader = csv.DictReader(fp)
    for x in reader:
        print(x)
