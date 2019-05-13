#!/usr/bin/python
l1=eval(input("enter first list"))
l2=eval(input("enter second liat"))
l3=[]
for i in l1:
   if i in l2:
    l3.append(i)
print("intersection of 2 lists is:",l3)



