# Creating a dictionary  
students = {1: 'Rahul', 2: 'Amit', 3: 'Neha', 4: 'Priya', 5: 'Sonia'}
print("Dictionary:", students)

# Adding a new entry  
students[6] = 'Rohan'
print("\nDictionary after adding a new student:", students)

# Updating a value  
students[3] = 'Pooja'
print("\nDictionary after updating a value:", students)

# Accessing a specific value  
print("\nAccessing a specific value:", students[1])

# Deleting a value  
del students[6]
print("\nDictionary after deleting a value:", students)

# Creating a nested dictionary  
student_details = {
    1: 'Rahul',
    2: 'Amit',
    3: {'Age': 20, 'Course': 'B.Tech', 'Year': 'Second'}
}
print("\nNested Dictionary:", student_details)

# Accessing a nested dictionary element  
print("\nAccessing an element from the nested dictionary:", student_details[3]['Course'])
