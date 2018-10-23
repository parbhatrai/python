
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



#PYTHON SCRIPT
import os
print("Home folder location is: ",os.environ['USERPROFILE'])
print("Hostname of the machine is: ",os.environ['USERDOMAIN'])
print("Current working directory is: ",os.environ['PYTHONPATH'])