# WRITE ROTATE FUNCTION HERE #
#                            #
#                            #
#                            #
#                            #
##############################
    
def rotate(nums,k):
    n = len(nums)
    
    if n == 0:
        return 0
    
    k = k % n
    
    last_part = nums[n - k:]
    first_part = nums[:n - k]
    
    nums[:] = last_part + first_part
    
    
    

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""