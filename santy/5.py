import csv
data={"roll no": ["1001","1002","1003"],"name":["Santiya","Athulya","Aiswarya"]}
with open("5.csv","w") as csv_file:
  writer=csv.DictWriter(csv_file,fieldnames=data.keys())
  writer.writeheader()
  for row in zip(*data.values()):
      writer.writerow(dict(zip(data.keys(),row)))
with open("5.csv") as csv_file:
   csv_reader=csv.DictReader(csv_file)
   for row in csv_reader:
       print(row)
