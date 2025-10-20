def main():
    N = int(input())
    for i in range(1, N+1):
        for j in range(1,N+2-i):
            print("*",end="")
        print("")
    return 0
if __name__ == '__main__':
    main()