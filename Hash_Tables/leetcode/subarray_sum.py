# WRITE SUBARRAY_SUM FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################

def subarray_sum(nums,target):
    sum_index = {0:-1}
    current_sum = 0
    for i,num in enumerate(nums):
        current_sum += num
        needed_sum = current_sum - target
        if needed_sum in sum_index:
            return[sum_index[needed_sum]+1,i]
        if current_sum not in sum_index:
            sum_index[current_sum] = i
    return []
            
        
    
    
    



nums = [1, 2, 3, 4, 5]
target = 9
print ( subarray_sum(nums, target) )

nums = [-1, 2, 3, -4, 5]
target = 0
print ( subarray_sum(nums, target) )

nums = [2, 3, 4, 5, 6]
target = 3
print ( subarray_sum(nums, target) )

nums = []
target = 0
print ( subarray_sum(nums, target) )



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 3]
    [0, 3]
    [1, 1]
    []

"""
