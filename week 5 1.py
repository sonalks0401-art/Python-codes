
# store minimum 5 elements in any data structure of your choice and display in stack.

data = [1, 2, 3, 4, 5]
stack = []
for i in data:
    stack.append(i)
print("Stack elements:")
while stack:
    print(stack.pop())



    def find132pattern(nums):
    stack = []
    second = float('-inf')   # this will be our "2"

    # go from right to left
    for i in range(len(nums)-1, -1, -1):

        # if we find 1
        if nums[i] < second:
            return True

        # update possible 2
        while stack and nums[i] > stack[-1]:
            second = stack.pop()

        # push as possible 3
        stack.append(nums[i])

    return False

# 132 pattern based question

def find132pattern(nums):
    stack = []
    second = float('-inf')   

    
    for i in range(len(nums)-1, -1, -1):
        if nums[i] < second:
            return True

        while stack and nums[i] > stack[-1]:
            second = stack.pop()

        # push as possible 3
        stack.append(nums[i])

    return False


