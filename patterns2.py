#ABCD
n = 4
num = 0
for i in range(n):
    for j in range(n):
        print(chr(65+j), end = " ")
    print()

for i in range(65,69):
    for j in range(4):
        print(chr(i),end = " ")
    print()
    
#AAAA,BBBB...
n = 6
num =0
for i in range(n):
    for j in range(n):
        print(chr(65+num),end = " ")
        num += 1
        if chr(65+num-1) == 'Z':
            num = 0
    print()
    
#A-Z
n = 6
num = 0
for i in range(n):
    for j in range(n):
        print(i+j+1,end = " ")
    print()
    
#program to show, if the number is even, print "=", odd= "+"
n = 4
for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            print("=", end=" ")
        else:
            print("+", end=" ")
    print()
    
#Aa Bb...
num = 0
for i in range(8):
    for j in range(4):
        print(chr(65+num) + chr(97+num), end=" ")
        num += 1
        if chr(65+num-1) == 'Z':
            if chr(97+num-1) == 'z':
                num=0
    print()        
