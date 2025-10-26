def isPalindrome(s):
    '''Input: s takes the string as input
       Output:return the True or False'''
    # YOUR CODE GOES HERE
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start+=1
        end-=1
    return True

    

