    T = int(input())
    
    # Iterate through each test case
    for _ in range(T):
        # Input the array
        arr_size, *arr = map(int, input().split())
        
        # Calculate and print the absolute difference
        print(absoluteDifference(arr))

if __name__ == '__main__':
    main()