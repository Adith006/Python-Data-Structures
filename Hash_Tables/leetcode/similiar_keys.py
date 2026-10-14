l1 = [1,2,3]
l2 = [2,3,5]

# def common_item(l1,l2):
#     for i in l1:
#         for j in l2:
#             if i == j:
#                 return True
#     return False

# print(common_item(l1,l2))

#hash function
def common_item(l1,l2):
    my_dict = {}
    for i in l1:
        my_dict[i] = True
    for j in l2:
        if j in my_dict:
            return True
    return False

print(common_item(l1,l2))


