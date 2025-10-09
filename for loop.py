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
#tasks
#find min element in list using for loop
#find max element in list using for loop
#find sum of elements in the list
#find the product of a list

#max element in list using for loop
lst=list(map(int,input().split()))
max_num=lst[0]
for i in range(len(lst)):
    if lst[i] > max_num:    
        max_num = lst[i]     
print("Max number is:", max_num)

#sum of elements in the list
lst=list(map(int,input().split()))
sum = 0
for num in lst:
    sum = sum + num
    print("sum of numbers: ",sum)

#product of elements in the list
lst=list(map(int,input().split()))
prod = 1
for num in lst:
    prod = prod * num
    print("product of numbers: ",prod)

    

