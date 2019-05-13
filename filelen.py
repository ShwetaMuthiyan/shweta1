#!/usr/bin/python

import io
f=input("enter file name:")
fd= io.FileIO(f)
line=fd.readline()
maxline= fd.readline()
minline=maxline
maxline=fd.readline()
if maxline>minline:
   print(maxline)
else: 
   print(minline)

while line!= b'':
  print(line)
  line=fd.readline()
print("maxline is:",maxline)
print("minline is:",minline)
