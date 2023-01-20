f1=open("sample.txt","r")
f2=open("sample1.txt","w")
l=f1.readlines()
for i in range(0,len(l),2):
  f2.write(l[i])
  print(l[i])
f2.close()
f1.close()



