def main():
    N = int(input())
    for i in range(N):
        for j in range(2*N):
            if j < N - i:
                print("*", end="")
            elif j < N - i + 2 * i:
                print(" ", end="")
                print("*", end="")                 
        print("")  # Move to the next line after each row
    return 0
if __name__ == '__main__':
    main()