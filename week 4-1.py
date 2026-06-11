
#Given an array of strings strs, group the anagrams together. You can return the answer in any order. 
  
def groupAnagrams(strs):
    anagram_dict = {}

    for word in strs:
        # sort the word
        key = ''.join(sorted(word))

         #store in dictionary
        if key not in anagram_dict:
            anagram_dict[key] = []

        anagram_dict[key].append(word)

          #return
    return list(anagram_dict.values())


# Example
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))


#You are given a large integer represented as an integer array digits

def plusOne(digits):

    n = len(digits)

    # start from last digit
    for i in range(n-1, -1, -1):

        if digits[i] < 9:
            digits[i] += 1
            return digits

        # if digit is 9
        digits[i] = 0

    # if all digits were 9
    return [1] + digits


# Example
print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))
print(plusOne([9,9,9,9]))

# Colour baesd problem,dutch national algorithm


def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


# Example
nums = [2,0,2,1,1,0]
print(sortColors(nums))

def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


# Example
nums = [2,0,2,1,1,0]
print(sortColors(nums))

# Example 
nums = [2,0,1] 
print(sortColors(nums))





