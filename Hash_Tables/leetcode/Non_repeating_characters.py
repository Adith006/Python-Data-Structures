# WRITE THE FUNCTION HERE #
#                         #
#                         #
#                         #
#                         #
###########################
def first_non_repeating_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char]+= 1
        else:
            char_count[char] = 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None
    
            
    


print( first_non_repeating_char('leetcode') )

print( first_non_repeating_char('hello') )

print( first_non_repeating_char('aabbcc') )



"""
    EXPECTED OUTPUT:
    ----------------
    l
    h
    None

"""
