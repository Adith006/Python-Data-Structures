# WRITE FIND_PAIRS FUNCTION HERE #
#                                #
#                                #
#                                #
#                                #
##################################

def find_pairs(arr1,arr2,target):
    seen = set()
    pairs = []
    for num in arr1:
        seen.add(num)
    for num in arr2:
        matching = target - num
        
        if matching in seen:
            pairs.append((matching,num))
    return pairs
        
    


arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 8, 10]
target = 7

pairs = find_pairs(arr1, arr2, target)
print (pairs)



"""
    EXPECTED OUTPUT:
    ----------------
    [(5, 2), (3, 4), (1, 6)]

"""