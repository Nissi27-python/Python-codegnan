#type conversions
#integer to string,float,boolean conversion
num=int(input())
print(num)
val=float(num)
print(val)
print(bool(num))
print("String type number:",str(num))

#float to integer,string,boolean
val=float(input())
print("integer conv:",int(val))
print("string conv:",str(val))
print("boolean conv:",bool(val))

#string to integer,float,,boolen,list,tuple and set conversions

string=input()
print("integer conv:",int(string))
print("float conv:",float(string))
print("bool conv:",bool(string))
print("list conv:",list(string))
print("tuple conv:",tuple(string))
print("set conv:",set(string))

#list to string,tuple,set conversion

list_nums=list(map(int,input().split()))
print(list_nums)
string_list=str(list_nums)
print(string_list)
print(string_list[:3])
print("tuple conv:",tuple(list_nums))
print("set conv:",set(list_nums))

#list to dictionary conversion
lst=[['a',1],['b',2],['c',3]]
print(dict(lst))

#tuple to list,string and set conversions
t=tuple(map(int,input().split()))
print("string conv:",str(t)[:5])
print("list conv:",list(t))
print("set conv:",set(t))

#set to list, string, tuple
s=set(map(int,input().split()))
print("string conv:",str(s)[:5])
print("list conv:",list(s))
print("tuple conv:",tuple(s))

#reading dict from user
n=int(input())
d={}
for i in range(n):
  key,value=map(int,input().split())
  d[key]=value
print(d)


      
