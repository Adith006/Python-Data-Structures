# WRITE FIND_DUPLICATES FUNCTION HERE #
#                                     #
#                                     #
#                                     #
#                                     #
#######################################

def find_duplicates(nums):
    num_count = {}
    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1
    duplicates = []
    for num in num_count:
        if num_count[num]>1:
            duplicates.append(num)
    return duplicates
    
    



print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )



"""
    EXPECTED OUTPUT:
    ----------------
    []
    [1, 2]
    [1]
    [3, 4]
    [1, 2, 3]
    [1, 2, 3]
    []

"""

