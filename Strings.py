# Different ways creating a string.

string = 'Hello'
print(string)

string = "Hello"
print(string)# Different ways of creating a string.

text1 = 'Hello'
print(text1)

text2 = "Hello"
print(text2)

text3 = '''World'''
print(text3)

text4 = """Welcome to
           the realm of Python""" # triple quotes allow multi-line strings
print(text4)
print()

# Concatenating two strings using + operator
concat_text = text1 + text3
print("Concatenated two different strings:", concat_text)
print()

# Finding the length of the string.
print("Length of the string:", len(concat_text))
print()

# Extracting a substring.

# Searching in strings using index()
search_text = 'developer'
sub_text1 = 'lop'
sub_text2 = 'e'
print("Position of 'lop':", search_text.index(sub_text1))
print("Position of 'e':", search_text.index(sub_text2))
print()

# Matching a String Against a Regular Expression With match().
import re
pattern = 'Naruto'
quote = 'Naruto once said - Believe it!'
print(re.match(pattern, quote))
print()

# Comparing strings.
string_a = 'Sasuke Uchiha'
string_b = 'Naruto Uzumaki'
string_c = string_a
print(string_a == string_b)
print(string_a == string_c)
print(string_b == string_c)
print(string_a != string_b)
print()

# startsWith(), endsWith().
hero = 'Jiraiya Sensei'
print(hero.startswith("Jiraiya"))
print(hero.endswith("Sensei"))
print()

# Trimming strings with strip().
text_trim = 'Welcome Home!'
print(text_trim.strip("!"))
print()

# Replacing characters in strings with replace()
greeting = 'Hey there'
print(greeting.replace("Hey", "Hello"))
print()

# Splitting strings with split()
message = 'apple-banana-cherry'
print(message.split("-"))
print()

# Converting integer objects to Strings.
number = 25
number_str = str(number)
print(number_str)
print(type(number_str))
print()

# Converting to uppercase and lowercase.
lower_text = 'good morning'
upper_text = 'EVENING'
print(lower_text.upper())
print(upper_text.lower())

string1 = '''World'''
print(string1)

string2 = """Welcome to
           the world of Python""" # triple quotes string can extend multiple lines
print(string2)
print()

# Concatenating two strings using + operator
str1 = string + string1
print("Concatenated two different strings:",str1)
print()

# Finding the length of the string.
print("length of the string:",len(str1))
print()

# Extract a string using Substring.

# Searching in strings using index()
str3 = 'kashish'
str1 = 'ish'
str2 = 'h'
print("Position of ish:",str3.index(str1))
print("Position of h:",str3.index(str2))
print()

# Matching a String Against a Regular Expression With matches().
from ast import Str
import re
Substr = 'Madara'
str6 = 'Madara once said- Wake up to relity nothing goes as planned in this cursed world'
print(re.match(Substr,str6))
print()

# Comparing strings.
str8 = 'Itachi uchiha'
str1 = 'Madara uchiha'
str2 = str8
print(str8 == str1)
print(str8 == str2)
print(str1 == str2)
print(str8 != str1)
print()

# startsWith(), endsWith().
string = 'Minato Namikaze'
print(string.startswith("Minato"))
print(string.endswith("kaze"))
print()

# Trimming strings with strip().
str7 = 'Hello World hi'
print(str7.strip("hi"))
print()

# Replacing characters in strings with replace()
string = 'Hi World'
print(string.replace("Hi","Hello"))
print()

# Splitting strings with split()
str9 = 'hi-hello-bye'
print(str9.split("-"))
print()

# Converting integer objects to Strings.
numb = 10
numb1 = str(numb)
print(numb1)
print(type(numb1))

print()
# Converting to uppercase and lowercase.
string = 'hello'
string1 = 'WORLD'
print(string.upper())
print(string1.lower())
