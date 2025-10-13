#square pattern
n=4
for i in range(4):
    for j in range(4):
        print(i+1,end=" ")
    print()
#2
n=4
for i in range(4):
    for j in range(4):
        print(j+1,end=" ")
    print()

#3
n=1
for i in range(4):
    for j in range(4):
        print(n,end=" ")
        n+=1
    print()
#4
n=1
for i in range(4):
    for j in range(4):
        print(i*n+j+1,end=" ")
    print()
