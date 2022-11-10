txt = input("Enter a string : ")
char = txt[0]
txt= txt.replace(char,'$')
print(char+txt[1:])
