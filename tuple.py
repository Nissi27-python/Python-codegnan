#tuple
t=(1,2,3,[10,20,30],"nissi")
print(t)

#t[0]=100 - type error

#read tuple of integers from user
t=tuple(map(int, input().split()))
print(t)

#index based and slicable
t=(1,2,3,[10,20,30],"Codegnan")
print(t[2],t[-2],t[-4])
print(t[-1:2:-1])
print(t[-1:2:1])
print(t[3:-4:-1])

#single element represtation in tuple
t=(30)
t2=(20,)
print(type(t),type(t2))

#tuple operations
1.concatination
t1=(1,2,3)
t2=('A','B')
t3=t1+t2
print(t3)

#2.repetation
t1=(1,2,3)
t=t1*3
print(t)

#tuple methods
#1.index(ele)-it returns index of element, otherwise ValueError
#2.count(ele)- it returns total occurance of element in tuple

t=(1,2,3,[10,20,30],"Codegnan")
ind=t.index(3)
count=t.count(3)
print(ind,count)

#builtin function
len(),min(),max(),sum()
t=(1,2,3,4,5)
print(len(t),min(t),max(t),sum(t))

#string to tuple conversion
s="Codegnan"
print(list(s))
print(tuple(s))
#tuple to list conversion
t=(1,2,3,4,5)
print(list(t))

