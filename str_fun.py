#String Operations
"""B. Removing spaces and characters
Method	Purpose	Example	Output
strip()	Removes leading and trailing whitespace	"  hi  ".strip()	'hi'
lstrip()	Removes leading whitespace	"  hi  ".lstrip()	'hi  '
rstrip()	Removes trailing whitespace	"  hi  ".rstrip()	'  hi'"""

text = "  Prerana  "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

#Remember: these methods return a new string. They do not modify the original string.
#String Operations
"""B. Removing spaces and characters
Method	Purpose	Example	Output
strip()	Removes leading and trailing whitespace	"  hi  ".strip()	'hi'
lstrip()	Removes leading whitespace	"  hi  ".lstrip()	'hi  '
rstrip()	Removes trailing whitespace	"  hi  ".rstrip()	'  hi'"""

text = "  Prerana  "

print(text.strip())
print(text.lstrip())
print(text.rstrip())

#Remember: these methods return a new string. They do not modify the original string.

"""
D. Replacing and splitting
Method	Purpose	Example	Output
replace()	Replaces text	"hello".replace("l", "x")	'hexxo'
split()	Splits into a list	"a,b,c".split(",")	['a', 'b', 'c']
rsplit()	Splits from the right	"a-b-c".rsplit("-", 1)	['a-b', 'c']
partition()	Splits at first separator into 3 parts	"a-b-c".partition("-")	('a', '-', 'b-c')
join()	Joins strings using a separator	"-".join(["a","b"])	'a-b'
"""

print("hello".replace("l","m"))
print("a,b,c".split(","))
print("hello".split(","))
print("hello".rsplit(","))
text = "hello"
for i in text:
    print(i)

print("a-b-c-d-e-f-e-d-e".rsplit("-",6))

"""
E. Checking string contents
These methods return Boolean values: True or False.
Method	Checks whether	Example	Output
isalpha()	All characters are letters	"Python".isalpha()	True
isdigit()	All characters are digits	"123".isdigit()	True
isnumeric()	All characters are numeric	"123".isnumeric()	True
isalnum()	All characters are letters or digits	"Python123".isalnum()	True
isspace()	All characters are whitespace	"   ".isspace()	True
islower()	Cased characters are lowercase	"hello".islower()	True
isupper()	Cased characters are uppercase	"HELLO".isupper()	True
istitle()	Text follows title-case rules	"Hello World".istitle()	True
isidentifier()	Valid Python identifier	"my_var".isidentifier()	True
isprintable()	All characters are printable	"Hello".isprintable()	True

Note: isdigit() and isnumeric() accept some Unicode numeric characters too. 
For ordinary positive integers in text, they work as expected.
"""

print("python".isalpha())
print("123".isdigit())
print("123".isnumeric())
print("py123".isalnum())
print(" ".isspace())
print("ashu".islower())
print("ASHU".isupper())
print("Ashu P.".istitle())
print("my_name".isidentifier())
print("prerana".isprintable())

"""
F. Alignment and formatting
Method	Example	Output
center()	"hi".center(6, "-")	'--hi--'
ljust()	"hi".ljust(5, "-")	'hi---'
rjust()	"hi".rjust(5, "-")	'---hi'
zfill()	"42".zfill(5)	`'00042'
format()	"My name is DIL1".format("Prerana")	'My name is Prerana'
"""

print("hello".center(16,"="))
print("hello".ljust(5,"="))
print("hello".rjust(5,"="))
print("55".zfill(10))
print("hello {name}".format(name="World"))

""" 
D. Replacing and splitting
Method	Purpose	Example	Output
replace()	Replaces text	"hello".replace("l", "x")	'hexxo'
split()	Splits into a list	"a,b,c".split(",")	['a', 'b', 'c']
rsplit()	Splits from the right	"a-b-c".rsplit("-", 1)	['a-b', 'c']
partition()	Splits at first separator into 3 parts	"a-b-c".partition("-")	('a', '-', 'b-c')
join()	Joins strings using a separator	"-".join(["a","b"])	'a-b'
"""

print("hello".replace("l","x"))
print("x,y,z".split(","))
print("a,a,a,a,a,a,a".rsplit(",",3))
print("m-n-no".partition("-"))
print("-".join(["a","b","c"]))