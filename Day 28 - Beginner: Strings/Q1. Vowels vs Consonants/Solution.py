def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    vowels = 0
    consonants = 0

    t= int(input()) # number of test cases

    for _ in range(t):
        s = input().lower()

        vowels = 0
        consonants = 0

        for char in s:
            if char.isalpha():
                if char in ('a','e','i','o','u'):
                    vowels += 1 
                else:
                    consonants += 1 
        
        print(vowels, consonants)

    return 0

if __name__ == '__main__':
    main()