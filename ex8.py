a=[2,5,-8,10,-5]
print("The list :")
print(a)
b=[x for x in a if x>0]
print("The postive number list from the above list : ")
print(b)

list=[]
n=int(input("enter the number of elements"))
for i in range(n):
    a=int(input())
    list.append(a)
print(list)
b=[i*i for i in list]
print("square :")
print(b)

a=input("enter a word  ")
b="aeiouAEIOU"
vowels=[each for each in a if each in b ]
print(vowels)

e=input("enter a word ")
f=[ord(c) for c in e]
print(f)
