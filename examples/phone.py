import re
# Returns first instance of phone number pattern:
def extract_phone(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	match = phone_regex.search(input)
	if match:
		return match.group()
	return None

# Returns all instances of phone number pattern in a list
def extract_all_phones(input):
	phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
	return phone_regex.findall(input)

# One way of checking if entire string is valid phone number:
# def is_valid_phone(input):
# 	phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
# 	match = phone_regex.search(input)
# 	if match:
# 		return True
# 	return False

# Another way of doing the same thing, using the fullmatch method
def is_valid_phone(input):
	phone_regex = r'\d{3} \d{3}-\d{4}'
	match = re.fullmatch(phone_regex, input)
	if match:
		return True
	return False

print(extract_phone("my number is 432 567-8976"))
print(extract_all_phones("my number is 432 567-8976 or call me at 345 666-7899"))
print(is_valid_phone("432 567-8976"))




