import csv
with open("3.csv",newline="") as f:
  s=csv.reader(f,delimiter=" ",quotechar="|")
  for i in s:
      print(" , ".join(i))
