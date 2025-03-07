# Function to add integer values of an array
arr = [10, 20, 30, 40]
sum_value = 0
for i in arr:
    sum_value += i
print("Sum of all integer values in array:", sum_value)

# Function to calculate the average value of an array
def calculate_average(arr):
    total = 0
    count = 0
    for i in arr:
        total += i
        count += 1
    avg = total / count
    return avg

print("The average is", calculate_average([10, 21, 32, 43, 54]))

# Function to find the index of an array element
arr = [1, 3, 5, 3, 1, 2, 6, 5, 3, 8, 6, 9]
element = 3
index = -1
for i in range(len(arr)):
    if arr[i] == element:
        index = i
        break
print("Index of", element, ":", index)

# Function to check if an array contains a specific value
arr = [4, 5, 45, 40, 50]
element = 5
found = False
for num in arr:
    if num == element:
        found = True
if found:
    print("Element exists")

# Function to remove a specific element from an array
arr = [44, 55, 0, 15, 19, 5, 4]
element_to_remove = 0
new_arr = []
for num in arr:
    if num != element_to_remove:
        new_arr.append(num)
print(new_arr)

# Function to copy an array to another array
arr = ['k', 'a', 's', 'h', 'i']
arr1 = []
for i in arr:
    arr1.append(i)
print(arr1)

# Function to insert an element at a specific position in an array
arr = [101, 303, 404, 505, 606, 707, 808, 909]
new_arr = []
position = 1
value = 202
for i in range(len(arr) + 1):
    if i < position:
        new_arr.append(arr[i])
    elif i == position:
        new_arr.append(value)
    else:
        new_arr.append(arr[i - 1])
print(new_arr)

# Function to find the minimum and maximum value of an array
arr = [100, 3, 3000, 20, 500, 9999, 10000, 10003]
min_value = arr[0]
max_value = arr[0]
for num in arr:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num
print("The minimum value is:", min_value)
print("The maximum value is:", max_value)

# Function to reverse an array
arr = [9, 8, 7, 6, 5]
reversed_arr = []
for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])
print(reversed_arr)

# Function to find duplicate values in an array
arr = [21, 11, 31, 13, 11]
duplicates = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j] and arr[i] not in duplicates:
            duplicates.append(arr[i])
print("Duplicate elements in given array:", duplicates)

# Function to find common values between two arrays
arr = ['k', 'a', 's', 'h', 'i']
arr1 = ['s', 'h', 'g']
common_values = []
for i in arr:
    for j in arr1:
        if i == j and i not in common_values:
            common_values.append(i)
print("Common values in given arrays:", common_values)

# Function to remove duplicate elements from an array
arr = [11, 22, 33, 11, 44, 55]
unique_arr = []
for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)
print(unique_arr)

# Function to find the second largest number in an array
arr = [101, 404, 202, 909, 606, 505, 808, 303, 707]
largest = arr[0]
second_largest = arr[0]
for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print("Second largest number:", second_largest)

# Function to count even and odd numbers in an array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_count = 0
odd_count = 0
for num in arr:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

# Function to get the difference between largest and smallest value
arr = [10, 6, 11, 13, 14]
min_value = arr[0]
max_value = arr[0]
for num in arr:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num
print("Difference of largest and smallest value:", max_value - min_value)

# Function to check if an array contains two specified elements (12, 23)
arr = [1, 12, 19, 23, 33, 54]
elements = [12, 23]
for num in arr:
    if num in elements:
        print(num, "exists in the array")
