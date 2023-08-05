
import time
from unicodedata import name
name = input("Name: ").lower()
while len(name)>0: 
    print(name)
    name=name.replace(input(),"",1)

#print(name)P

