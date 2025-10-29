def absoluteDifference(arr):
    # Initialize counters for even and odd elements
    even_count = 0
    odd_count = 0
    
    # Iterate through the array
    for num in arr:
        # Check if the number is even
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Calculate the absolute difference
    return abs(even_count - odd_count)

# Main function
def main():
    # Input the number of test cases
    T = int(input())
    
    # Iterate through each test case
    for _ in range(T):
        # Input the array
        arr_size, *arr = map(int, input().split())
        
        # Calculate and print the absolute difference
        print(absoluteDifference(arr))

if __name__ == '__main__':
    main()