def change_char(s):
    '''Input: s takes the string as input
       Output:return the resultant string'''
       
    res = ''
    # YOUR CODE GOES HERE
    first_char = s[0]
    res = first_char+s[1:].replace(first_char,"$")
    
    return res
    

