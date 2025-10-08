# 1.old style output formatting-using comma
name="nissi"
age=21
print("Name is",name,"and age is",age+1)

#2.modulo operator output formatting-using access specifiers

##%d-integers
##%f-float
##%s-string
name ="Nissi"
age=21
print("Name is %s and age is %d"%(name,age))

##name ="Nissi"
##age=21
##print("Name is %s and age is %d"%(age,name))-raises ype error

#3. dot format-using dot
name ="Nissi"
age=21
print("Name is {} and age is {}".format(name,age))
print("Name is {} and age is {}".format(age,name))
print("Name is {1} and age is {0}".format(name,age))
print("Name is {0} and age is {1}".format(name,age))
print("Name is {0} and age is {1}".format(age,name))
print("Name is {1} and age is {0}".format(age,name))

#4.f-format
name ="Nissi"
age=21
percentage=98.52
print(f"Name is {name} and age is {age} and i have {percentage}")
print(f"Name is {name} and age is {age} and i have {percentage:.1f}")
num=2
print(f"{num:{5}d}")
print(f"{num:0{5}d}")
print(f"{num:{5}d}")

#eval() function
res=eval('52+3')
print(res)
print('52+3')
print(eval('53+3'))

num=eval(input())
print(type(num),num)

l=list(map(int,input().strip().split()))
print(l)

s=input().strip().split()
print(s)
l=list(map(int,s))
print(l)


