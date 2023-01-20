import csv
with open("3.csv",newline="") as f:
  s=csv.DictReader(f)
  for i in s:
      print(i["student_id"],i["name"])
