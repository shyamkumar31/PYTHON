arr = [1, 2, 3]
try:
    print("Second element =", arr[1])

    # Throws error since there are only 3 elements in the list
    print("Fourth element =", arr[3])

except:
    print("An error occurred")

print()

list1 = [3, 2, 1]
list2 = [1, 2, 3]
try:
    list1 == list2
except:
    print("They are not equal")
else:
    print("Both Equal")

print()

try:
    result = 5 / 0
    print(result)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print("This is always executed")
