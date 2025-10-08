#print 1-n numbers
n=int(input())
i=1
while i<n:
    print(i)
    i+=1
else:
    print("Program done")
#remove an element in a list
lst = [1,2,2,3,2,1]
ele=2
n=len(lst)
i=0
while i<n:
    if lst[i]==ele:
        lst.pop(i)
        n-=1
    else:
        i+=1
print(lst)


#find min element in list using for loop
#find max element in list using for loop
#find sum of elements in the list
#find the product of a list
