#!/bin/usr/python

x=eval(input("enter the input list"))
print(x)
print (len(x))

def max():
    for i in range (len(x)):  
    max=x[0]
   if( x[i+1]>x[i]):
     max=x[i+1]
  else:
     max=x[i]

print (max)
max()




#write a program implement stack using list.

