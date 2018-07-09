import os
x5=0
for x1,x2,x3 in os.walk(r"F:\软件库"):
    for x4 in x3:
        x5+=1
        print(x4)
print(x5)