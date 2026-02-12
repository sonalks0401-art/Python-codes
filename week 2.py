
# #1. Find the kth smallest element element in a given array - QUICKSELECT

# arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
# k = 4

# arr_sort = sorted(arr)
# print(arr_sort[k-1])


#2. The arr contains height of towers and we 'have' to adjust there height either add or substract 'k.. AND find the minimum height difference (They are sorted?)
# We need to substract from the highest number and add in lowest number so that the difference can be minute

k_elem = 2
my_arr = [1, 5, 8, 10]

# Greedy Approach

def find_elem(arr, k):
    arr.sort()
    n = len(arr)
    ans = arr[-1] - arr[0] # Fall back plan if the things doesnt go well
    
    for i in range(1, n):
        if arr[i] - k < 0:  #Check negative number
            continue
        
        min_ht = min(arr[0] + k, arr[i] - k)
        max_ht = max(arr[i-1] + k, arr[-1] - k)
        
        ans = min(ans, max_ht - min_ht)
    
    
    return ans

print(find_elem(my_arr, k_elem))