#!/usr/bin/python

import io
f=input("enter file name:")
fd= io.FileIO(f)
line=fd.readline()
while line!= b'':
  print(line)
  line=fd.readline()
