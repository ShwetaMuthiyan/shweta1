#!/usr/bin/python


def push(1,data):
    1.append(data)

def pop(1):
    return 1.pop()

def peep(1):
    return 1[-1]

def i is_empty(1):
    return 1==[]

def is_full(1):
    return len(1)==10

def menu():
    ch=-1
    while ch <1 or ch >4:
        print("welcome to stack menu")
        print("1.push\n2.pop\n3.peep\n4.exit")
        ch=eval(input("enter choice"))

    return ch
def stack_operations():
    1=[]
    ch=menu()
    while(ch!=4):
       if ch==1:
          if not is_full(1):
             push(1,eval(input("enter data to push")))

          else:
             print("please pop something,stack is full")

       elif ch==2:
            if not is_empty(1):
               print(pop(1))
            else:
              print("stack is empty")

       elif ch==3:
            if not is_empty(1):
               print(peep(1))
             else:
               print("stack is empty")

             else:
                  break
             ch=menu()

def main():
    stack_operations()
if _name_== "_main_":
     main()



 
  





