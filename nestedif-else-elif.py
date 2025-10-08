num=int(input())
if num > 0 and num % 2 == 0:
    print("positive and even")
elif num < 0 and num % 2 == 0:
    print("negative and even")
elif num > 0 and num % 2 != 0:
    print("positive and odd")
else:
    print("negative and odd")

#nested if
num=int(input())
if num > 0:
    if num % 2 == 0:
        print("postive and even")
    else:
        print("positive and odd")
else:
    if num < 0:
        print("negative and odd")
    else:
        print("negative and even")
        
#biggest of three numbers(if-else)
n1,n2,n3=map(int,input().split())
if n1 > n2 and n1 > n3:
    print("n1 is bigger")
elif n2 > n1 and n2 > n3:
    print("n2 is bigger")
else:
    print("n3 is bigger")
    
#nested if
n1,n2,n3=map(int,input().split())
if n1 > n2:
    if n1 > n3:
        print("n1 is bigger")
    else:
        print("n3 is bigger")
else:
    if n2 > n3:
        print("n2 is bigger")
    else:
        print("n3 is bigger")


#example program using if-else statement
num=int(input())
if num < 10 and num % 2 == 0:
    print("small even")
else:
    print("big odd")
    
#example program using if-elif-else
num=int(input())
if num < 10 and num % 2 == 1:
    print("small odd")
elif num > 10 and num % 2 == 0:
    print("big and even")
else:
    print("other")

#example program using nested if
num=int(input())
if num < 10:
  if num % 2 == 1:
    print("small")
  else:
    print("other")
else:
    if num % 2 ==0:
      print("big")
    else:
      print("other")





