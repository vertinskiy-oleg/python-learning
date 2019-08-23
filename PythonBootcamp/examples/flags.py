import re
# Inline flags
pattern = re.compile(r"""(?i)(?x) #(?i) - ignorcase flag, (?x) - verbose flag
	^([a-z0-9_\.-]+)
	@
	([0-9a-z\.-]+)
	\.
	([a-z\.]{2,6})$
	""")

# Flags in compile() method
pattern = re.compile(r"""
	^([a-z0-9_\.-]+)	#first part of email	
	@					#single @ sign
	([0-9a-z\.-]+)		#email provider
	\.					#single period
	([a-z\.]{2,6})$		#com, org, net, etc.
""", re.X | re.I) # re.I - ignorecase flag, re.X - verbose flag

#Flags in re methods
regex = (r"""
	^([a-z0-9_\.-]+)
	@
	([0-9a-z\.-]+)
	\.
	([a-z\.]{2,6})$""")
match = re.search(regex, "ThomaS123@Yahoo.com", flags = re.I|re.X) # re.I - ignorecase flag, re.X - verbose flag
print(match.group())
print(match.groups())