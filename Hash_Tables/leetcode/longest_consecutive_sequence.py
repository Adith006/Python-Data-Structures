# WRITE LONGEST_CONSECUTIVE_SEQUENCE FUNCTION HERE #
#                                                  #
#                                                  #
#                                                  #
#                                                  #
####################################################

def longest_consecutive_sequence(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_lenght = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_lenght += 1
            longest = max(longest,current_lenght)
    return longest
        

    
    
    


print( longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) )



"""
    EXPECTED OUTPUT:
    ----------------
    4

"""