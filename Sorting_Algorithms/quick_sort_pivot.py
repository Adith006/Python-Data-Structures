def swap(my_list,idx1,idx2):
    temp = my_list[idx1]
    my_list[idx1] = my_list[idx2]
    my_list[idx2] = temp

def pivot(my_list,pivot_idx,end_idx):
    swap_idx = pivot_idx

    for i in range(pivot_idx+1,end_idx+1):
        if my_list[i] < my_list[pivot_idx]:
            swap_idx += 1
            swap(my_list,swap_idx,i)
    swap(my_list,pivot_idx,swap_idx)
    return swap_idx

my_list = [4,6,1,7,3,2,5]

print(pivot(my_list,0,6))

print(my_list)