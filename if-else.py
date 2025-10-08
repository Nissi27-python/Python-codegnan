#check whether the number is zero

n=int(input())
if n==0:
  print("number is zero")
print("program done")

#if-else
age=int(input())
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")

#example
stock=int(input())
price=int(input())
sel_product=int(input("count of product:"))
amount_paid=int(input("amount paid:"))
total_amount=price*sel_product
if stock>=sel_product and total_amount<=amount_paid:
    print("remaining amount:",amount_paid-total_amount)
else:
    print("insufficient")

#even number
n=int(input())
if n%2==0:
      print("even")
else:
    print("odd")
    
#find odd and even in 3 numbers
n1,n2,n3=map(int,(input().split()))
if n1 % 2 == 0:
    print("even")
else:
    print("odd")
if n2 % 2 == 0:
    print("even")
else:
    print("odd")
if n3 % 2 == 0:
    print("even")
else:
    print("odd")

#positive negative
n=int(input())
if n>=0:
    print("positive")
else:
    print("negative")
    
#task
    #0 or non 0
    #check whether the number is divisible by 5
    #check whether the number divisible with 4 or 5
    #check whether the number is factor for 6 or not
    
#0 or non 0
n=int(input())
if n==0:
      print("number is zero")
else:
      print("number is non-zero")
      
#divisible of 5
n=int(input())
if n%5==0:
      print("number is divisible by 5")
else:
      print("number is not divisibe by 5")
      
#divisible by 4 or 5
n=int(input())
if n%4==0 or n%5==0:
      print("yes")
else:
      print("no")

#factor of 6
if 6 % num == 0:
    print(num, "is a factor of 6")
else:
    print(num, "is not a factor of 6")
    
