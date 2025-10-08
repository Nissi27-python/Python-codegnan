#reading dict from user
n=int(input())
d={}
for i in range(n):
  key,value=map(int,input().split())
  d[key]=value
print(d)
