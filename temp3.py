
# Given an array arr, rotate the array by one position in clockwise direction. 
 

arr = [1, 2, 3, 4, 5]
n = len(arr)

last = arr[n - 1]

for i in range(n - 1, 0, -1):
    arr[i] = arr[i - 1]

arr[0] = last

print(arr)

# Second version

arr = [1, 2, 3, 4, 5]

arr = [arr[-1]] + arr[:-1]

print(arr)


# You are given an integer array arr[]. You need to find the maximum sum of a subarray (containing at least one element) in the array arr[]. 


arr = [2, 3, -8, 7, -1, 2, 3]

current_sum = arr[0]
max_sum = arr[0]

for i in range(1, len(arr)):
    current_sum = max(arr[i], current_sum + arr[i])
    max_sum = max(max_sum, current_sum)

print(max_sum)

#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in 
#order.  

#
nums = [1, 3, 5, 6]
target = 5

low = 0
high = len(nums) - 1

while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
else:
    print(low)


#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 

# Hash map

nums = [2, 7, 11, 15]
target = 9

seen = {}

for i in range(len(nums)):
    remaining = target - nums[i]

    if remaining in seen:
        print([seen[remaining], i])
        break
    else:
        seen[nums[i]] = i


#You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position. 

#Greedy Approach

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)

# Edge cases
if n == 1:
    print(0)
elif arr[0] == 0:
    print(-1)
else:
    max_reach = arr[0]
    steps = arr[0]
    jumps = 1

    for i in range(1, n):
        # If we reached the end
        if i == n - 1:
            print(jumps)
            break

        max_reach = max(max_reach, i + arr[i])
        steps -= 1

        # If no more steps left
        if steps == 0:
            jumps += 1

            if i >= max_reach:
                print(-1)
                break

            steps = max_reach - i









