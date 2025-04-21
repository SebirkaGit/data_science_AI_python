import sys
import re

print(sys.version)


print('Hello, World!')

s1 = "The BodyGuard 1 is the best album"

# Define the pattern to search for
pattern = r"\D"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")

# Matches any ten consecutive digits
pattern = r"\d\d\d\d\d\d\d\d\d\d"
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")

pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)


name = "John"
age = 50
# Formatted string output when using str.format()
# The colon (:) is used within {} to define how the value should
# be formatted when displayed. In your code, it is not explicitly used,
# but you can add it to control the output format if needed.
print("My name is {} and I am {} years old.".format(name, age))
print("{:<10}".format("John"))  # Left-align
print("{:>10}".format("John"))  # Right-align
print("{:^10}".format("John"))  # Center-align
print("{:.2f}".format(3.14159))  # Limit to 2 decimal places
print("{:06}".format(42))        # Pad with zeros to make it 6 digits

name1 = "Johnathan"
age1 = 30
print("My name is %s and I am %d years old." % (name1, age1))

regular_string = "C:\new_folder\file.txt"
print("Regular String:", regular_string)

raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)
