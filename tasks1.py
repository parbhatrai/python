
#TASKS Q1 TO Q6
q1 = [123, 354, 324, 2340, 324, 234, 756, 955]
max=0
for i in q1:
   if i>max:
       max=i
 print(max)

q2 = [432, 435, "588", "464", 234]
for x in q2:
    int_values = int(x)
    print(int_values)


q3 = {"K1": "V1", "K2": "V2", "K3": "V3"}
new_q3 = {v: k for k,v in q3.items()}
print(new_q3)


q6 = [33, 56, 76, 78, 34, 56]

for i in q6:
    if i % 3 == 0 and i % 5 == 0:
        print (str(i) + "FIZZBUZZ")
    elif i % 3 == 0:
        print (str(i) + "FIZZ")
    elif i % 5 == 0:
        print (str(i) + "BUZZ")
    else:
        print (str(i) + "Not divisible by 3 or 5")


#FUNCTIONS
def formatter(text):
    return "****\n" + text + "\n******"

def printwithformatter(formattingfunction, text):
    print(formattingfunction(text))

printwithformatter(formatter, "Hello")


#PARTIAL FUNCTIONS
from functools import partial
#normal function
def sumof(a, b):
    return(a + b)

print(sumof(1, 2))

plustwo = partial(sumof, 2)
print(plustwo(1))


#CREATING RANDOM GROUPS
import random
members=["x","y","z","P","L","K","R","T"]
groups=1
membersinthegroup=4

for member in members[:]:
    if membersinthegroup==4:
        print("Group {} consists of;".format(groups))
        membersinthegroup=0
        groups+=1
    person=random.choice(members)
    print(person)
    membersinthegroup+=1
    members.remove(str(person))



#PRINT PRIME NUMBERS FROM 1 TO N
limit = int(input("Enter a number:"))
for num in range(0, limit + 1):
    count = 0
    for i in range(2, (num//2 + 1)):
        if(num % i == 0):
            count = count + 1
            break

    if (count == 0 and num != 1):
        print(" %d" %num, end = '  ')


#CAT COMMMAND
def pycat(name):
    f = open(name, "r")
    readfile = print(f.read())
    f.close()

pycat("test.txt")


#MKDIR COMMAND
import os
def pymkdir(name):
    if os.path.isdir(name):
        print('Error: file already exists')
    else:
        os.mkdir(name)

pymkdir("/Users/Administrator/Desktop/project")