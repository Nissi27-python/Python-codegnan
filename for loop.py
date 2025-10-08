#print numbers
for num in range(1,11):
    print(num,end=" ")
else:
    print("Program done")

#even numbers
for num in range(0,101,2):
    print(num,end=" ")

#table
n=int(input())
for i in range(1,11):
    print(f"{n}*{i}={n*i}")

#find even numbers in a list
lst=[2,5,7,8,9]
res=[]
for i in range(len(lst)):
    if lst[i] % 2 == 0:
        res.append(lst[i])
print(res)
    
