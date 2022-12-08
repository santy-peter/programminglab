def fibanocci():
    n=int(input("enter the limit"))
    print("FIBANOCCI SERIES")
    a=0
    b=1
    print(a)
    print(b)
    for i in range(0,n):
        c=a+b
        a=b
        b=c
        print(c)
print(fibanocci())
