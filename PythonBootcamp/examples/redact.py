import re
text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"
regex = r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+'

#Using sub method on Regular Expression Object
# pattern = re.compile(regex, re.I)
# result = pattern.sub("\g<1> \g<2>", text)

#Using sub method on re module
result = re.sub(regex, "\g<1> \g<2>", text, flags=re.I) #\g<1> - refers to a first group, \g<2> - to the second

print(result) # Last night Mrs. D and Mr. w murdered Ms. C

