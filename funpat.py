#!/usr/bin/pythonl

def pattern():
 x=eval(input("numbers of lines to be printed: "))
 for i in range (x):
   for j in range(i+1):
     print("*", end=" ")
   print("\r")

pattern()

 
def pattern1():
   y=eval(input("numbers of lines to be printed: "))
   k=y*2-1
   for i in range(y):
     for j in range(k):
       print(end=" ")
     k=k-2
     for j in range (i+1):
        print("*", end=" ")
     print("\r")

pattern1()

 
def pattern2():
   z=eval(input("numbers of lines to be printed: "))
   k=z*2-2
   for i in range(z):
     for j in range(k):
       print(end=" ")
     k=k-1
     for j in range (i+1):
        print("*", end=" ")
     print("\r")

pattern2()



 
