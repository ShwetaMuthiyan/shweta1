#!/usr/bin/python

l1=eval(input("enter first list"))
l2=eval(input("enter second list"))
l3=[]
l3=l1
for x in l2:
   if x not in l3:
    l3.append(x)
   

print("union of list:",l3)
    
     

