def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    T = int(input())
    for _ in range(1,T+1):
        S = input()
        print(len(S))

    return 0

if __name__ == '__main__':
    main()