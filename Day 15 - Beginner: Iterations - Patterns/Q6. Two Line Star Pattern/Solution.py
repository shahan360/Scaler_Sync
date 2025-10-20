def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    for i in range(N):
        print("*", end='') # Print the first asterisk without a newline
        for j in range(N-2):
            print(" ",end='') # Print spaces without a newline
        print("*") # Print the last asterisk with a newline     
    return 0

if __name__ == '__main__':
    main()