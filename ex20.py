n=int(input("Enter the number of elements in list : "))
lists=[]
for i in range(n):
    value=int(input("Enter a number :"))
    lists.append(value)
print("The original list                    :",lists)
    
test = [each for each in lists if (each%2)!=0]
print("The list after removing even numbers :",test)


