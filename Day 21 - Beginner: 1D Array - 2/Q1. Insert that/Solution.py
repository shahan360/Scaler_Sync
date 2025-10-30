# Your Code Goes Here
N = int(input())
a=[]
s=input().split()
for i in range(N):
    a.append(int(s[i]))
X=int(input())
Y=int(input())
a.insert(X-1,Y)
for i in a:
    print(i, end=' ')    