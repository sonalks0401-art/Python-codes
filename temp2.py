#You are given an array of integers arr[]. You have to reverse the given array. 


arr = [1, 4, 3, 2, 6, 5]

i, j = 0, len(arr) - 1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1

print(arr)


# Given an array arr[]. Your task is to find the minimum and maximum elements in the array.


arr = [1, 4, 3, 5, 8, 6]
mn = mx = arr[0]

for x in arr:
    if x < mn: mn = x
    if x > mx: mx = x

print([mn, mx])

# Given an integer array arr[] and an integer k, your task is to find and return the kth smallest element in the given array.

arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

arr.sort()
print(arr[k-1])

# You are given two arrays a[] and b[], return the Union of both the arrays in any order.

a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

union = []


for i in a:
    if i not in union:
        union.append(i)


for j in b:
    if j not in union:
        union.append(j)


union.sort()

print(union)

  #second version

a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

union = list(set(a + b))
print(sorted(union))


# Given an array arr[]. The task is to find the largest element and return it.

arr = [1, 8, 7, 56, 90]

largest = arr[0]

for x in arr:
    if x > largest:
        largest = x

print(largest)




