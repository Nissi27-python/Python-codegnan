#example
num1=int(input())
num2=int(input())
if num1>num2:
    print(f"{num1} is bigger")
else:
    print(f"{num2} is bigger")

#greatest number
num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2 and num1>num3:
    print(f"{num1} is bigger")
elif num2>num1 and num2>num3:
    print(f"{num2} is bigger")
else:
    print(num3,"is bigger")

#samller number
num=int(input())
if num%2==0 and num>0:
    print("positive and even")
elif num%2==1 and num>0:
    print("positive and odd")
elif num%2==0 and num<0:
    print("negative and even")
elif num%2==1 and num<0:
    print("negative and odd")
else:
    print("zero")

#example
array=[1,2,3,4]
num=5
if num in array:
    print("yes")
else:
    print("no")
#example program of electricity bill
units=int(input())
if units <= 100:
    print(units * 1.5)
elif units > 300:
    print(units * 4)
elif units >= 200:
    print(units * 2.5)
else:
    print(units * 3)   
