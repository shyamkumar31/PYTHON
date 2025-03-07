# Reading from a text file
with open("HW.txt", "r") as hw_file:
    hw_data = hw_file.read()
    print(hw_data)

print()

# Writing to a text file
with open("Blank.txt", "w") as blank_file:
    text_to_write = 'Python'
    blank_file.write(text_to_write)

print()

# Reading with read+ mode (reading and writing)
with open("HW.txt", "r+") as hw_file_rp:
    print(hw_file_rp.readline(11))

print()
