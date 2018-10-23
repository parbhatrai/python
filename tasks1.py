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