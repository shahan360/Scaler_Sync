# write here

N = int(input())
for i in range(1,N+1):
    for k in range(i):
        print("*",end="")

    for p in range(1,2*(N-i)+1):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print("")