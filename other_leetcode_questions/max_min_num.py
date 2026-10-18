# WRITE FIND_MAX_MIN FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################
    
def find_max_min(my_list):
    max_num = my_list[0]
    min_num = my_list[0]
    for num in my_list:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return(max_num,min_num)
    

print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""