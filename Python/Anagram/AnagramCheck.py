from unicodedata import name

while True:
    Name=input("Name: ")
    NameO=Name
    Name2=input("Name2: ")
    Name2O=Name2
    Name.lower()
    Name2.lower()
    i=0
    k=0
    NameLength=len(Name)

    if len(Name)==len(Name2): 
        while len(Name)>0:
            if Name[0]==Name2[i]:
                Name=Name.replace(Name2[i],"",1)  
            i=i+1
            if i==len(Name2):
                i=0
                if NameLength==len(Name):
                    print("Not Anagram")
                    break

        print(NameO+" and "+Name2O+" are Anagram")
    else:
        print("Not Anagram")