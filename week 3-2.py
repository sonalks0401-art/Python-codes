# MEDIAN OF ARRAY



def find_median(arr):
    # Step 1: sort array
    arr.sort()

    n = len(arr)

    # Step 2: check odd or even
    if n % 2 == 1:        # Odd number of elements
        median = arr[n // 2]
    else:                 # Even number of elements
        median = (arr[n//2 - 1] + arr[n//2]) / 2

    return median


# Examples
print(find_median([90, 100, 78, 89, 67]))
print(find_median([56, 67, 30, 79]))
print(find_median([1, 2]))

#2D array assumihg 1D array.




def searchMatrix(matrix, target):

    m = len(matrix)
    n = len(matrix[0])

    low = 0
    high = m*n - 1

    while low <= high:

        mid = (low + high) // 2

        r = mid // n
        c = mid % n

        if matrix[r][c] == target:
            return True

        elif matrix[r][c] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

# Rectangular spiral traversal.



def spiral(matrix):
    top, bottom = 0, len(matrix)-1
    left, right = 0, len(matrix[0])-1
    result = []

    while top <= bottom and left <= right:

        # top row
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1

        # right column
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1

        # bottom row
        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # left column
        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left += 1

    return result




