def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    C = list(map(int,input().split()))
    A = C[0]
    B = C[1]
    while B>0:
        A,B = B,A%B

    print(A)        

    return 0

if __name__ == '__main__':
    main()