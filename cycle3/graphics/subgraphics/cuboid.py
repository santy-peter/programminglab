l=int(input("enter the length of cuboid"))
b=int(input("enter the breadth of cuboid"))
h=int(input("enter the height of cuboid"))
def cubTSA(l,b,h):
    print("Total surface area of cuboid = ",2*((l*b)+(b*h)+(h*l)))
def  cubperi(l,b,h):
    print("Perimeter of cuboid = ",4*(l+b+h))
cubTSA(l,b,h)
cubperi(l,b,h)
