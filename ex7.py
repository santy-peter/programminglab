a=input("enter the elements of list1 ").split(" ")
a=list(map(int,a))
print(a)
b=input("enter the elements of list2 ").split(" ")
b=list(map(int,b))
print(b)
n=len(a)
m=len(b)
if(n==m):
    print("both the list are of same length")
else:
    print("both the list are of different length")
sum1=0
sum2=0
for i in range(n):
    sum1=sum1+a[i]
for i in range(m):
    sum2=sum2+b[i]
print("sum of list1 = ",sum1)
print("sum of list2 = ",sum2)
if(sum1==sum2):
   print("both have same sum ")
else:
   print("both have different sum ")
 
for i in a:
    for i  in b:
        f=1
if f==1:
   print(i,"  occur in both lists")
else:
  print("values does not occur in both lists")
    
