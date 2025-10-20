def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N = int(input())
    for i in range(N):
        for j in range(2*N):
            # Print stars on the left side
            if j < N - i:
                print("*", end="")
            # Print spaces in the middle
            elif j < N - i + 2 * i:
                print(" ", end="")
            # Print stars on the right side
            else:
                print("*", end="")                 
        print("")  # Move to the next line after each row
    return 0

if __name__ == '__main__':
    main()