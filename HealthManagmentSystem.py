# Health Management System
# 3 clients - Shubh, Ramand Hari

def getdate():
    import datetime
    return datetime.datetime.now()

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            value=input("type here\n")
            with open("shubh-ex.txt","a") as op:
                op.write(str([str(gettime())])+": "+value+"\n")
            print("successfully written")
        elif(c==2):
            value = input("type here\n")
            with open("shubh-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("ram-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        
        elif (c == 2):
            value = input("type here\n")
            with open("ram-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
            
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("hari-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("hari-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")
def retrieve(k):
    if k==1:
        c=int(input("enter 1 for excersise and 2 for food"))
        if(c==1):
            with open("shubh-ex.txt") as op:
                for i in op:
                    print(i,end="")
        elif(c==2):
            with open("shubh-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("shubh-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("shubh-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k==3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("shubh-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("hari-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (shubh,ram,hari)")
print("health management system: ")
a=int(input("Press 1 for log the value and 2 for retrieve "))

if a==1:
    b = int(input("Press 1 for shubh 2 for hari 3 for ram "))
    take(b)
else:
    b = int(input("Press 1 for shubh 2 for hari 3 for ram "))
    retrieve(b)
  
