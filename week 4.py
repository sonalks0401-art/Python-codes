
# BASIC OPERTAION ON STRING


  #Indexing

arr = [10, 20, 30, 40, 50]
print(arr[0])   
print(arr[2])   
print(arr[4])  
print(arr[-1])
print(arr[-2])

  #Slicing
    
    #list[start : end : step]

arr = [10, 20, 30, 40, 50, 60]

print(arr[1:4])
print(arr[2:3])
print(arr[:3])     
print(arr[2:])     
print(arr[::2])    
print(arr[::-1])   

  #Modification by replacing

arr = [10, 20, 30, 40]

arr[1] = 99
print(arr)

  #Concatenation

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2
print(result)

  #Searching an element

arr = [10, 20, 30, 40]

print(arr.index(30))


arr = [10, 20, 30, 40]

print(20 in arr)
print(50 in arr)



