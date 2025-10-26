def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    u_count = 0
    l_count = 0
    for char in (input()):
        if 65<=ord(char)<=90:
            u_count+=1
        elif 97<=ord(char)<=122:
            l_count+=1
    print(u_count)
    print(l_count)  

    return 0

if __name__ == '__main__':
    main()