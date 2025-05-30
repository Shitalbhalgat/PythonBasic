# comparison of string
a = "Python"
b = "python"

print("a==b", a==b)
print("a!=b", a!=b)
print("a>b", a>b)
print("a<b", a<b)
print("a>=b", a>=b)
print("a<=b", a<=b)

#
a = "Python@12345"
b = "Python@12345"

print("a==b", a==b)
print("a!=b", a!=b)
print("a>b", a>b)
print("a<b", a<b)
print("a>=b", a>=b)
print("a<=b", a<=b)


#traversing of string
a="hello world"
for i in a:
    print(i,end="")

#built-in  method of strings
a="hElLo WoRlD"
print(a*3)
print("hi "+a)
print("length of string is : ", len(a))

#String Methods For Manipulating Case
print("capitalize() : ",a.capitalize())
print("upper(): ",a.upper())
print("lower(): ",a.lower())
print("swapcase(): ",a.swapcase())
print("title: ",a.title())
print("casefold: ",a.casefold())

s1 = "Straße"     # German word for "street" 
print("lower with german: ",s1.lower())    
print("casefold with german: ",s1.casefold())

print("Center(width): ",a.center(10))
print("Center(width,fillchar): ",a.center(10,'*'))
print("count(string) : ","12345634432122".count("2"))
print("count(string,start,end) : ","12345634432122".count("2",5,10))

# endswith() : It returns True if a string ends with the specified suffix.otherwise it returns False.
print("endswith(suffix) : ","123453578931".endswith("1"))
print("endswith(suffix,start,end) : ","123453578931".endswith("3",5,10))
# startswith() : It returns True if a string starts with the specified prefix.otherwise it returns False.
print("startswith(prefix) : ","123453578931".startswith("1"))
print("startswith(prefix,start,end) : ","123453578931".startswith("3",5,10))


# returns the index of first occurrence of the substring (if found),otherwise it returns -1.
a="h e l l o  w o r l d "
print("find(substring) : ",a.find("e"))
print("find(substring,start,end) : ",a.find("l",2,4))

# returns the index of last occurrence of the substring (if found),otherwise it returns -1.
print("rfind(substring) : ",a.rfind("l"))
print("rfind(substring,start,end) : ",a.rfind("l",2,4))

# returns the index of first occurrence of the substring (if found),otherwise it raises ValueError.
print("index(substring) : ",a.index("e"))
print("index(substring,start,end) : ",a.index("l",2,4))

# returns the index of last occurrence of the substring (if found),otherwise it raises ValueError.
print("rindex(substring) : ",a.rindex("l"))
print("rindex(substring,start,end) : ",a.rindex("l",2,4))

# isalnum() : It returns True if all characters in the string are alphanumeric (letters and numbers),otherwise it returns False.
print("isalnum(): ","12345a".isalnum())

print("isalpha() : ","12345a".isalpha())

#isdecimal() : Most strict; only decimal digits, no superscripts, fractions, or Roman numerals.
print("isdecimal() : ","12345a".isdecimal())

# isdigit(): includes decimal digits plus digits like superscript ² (²), and some Unicode digits.
print("isdigit() : ","12345².".isdigit())


#isnumeric(): includes decimal characters, digits, and fractions
print("isnumeric() : ","12345².".isnumeric())

#isidentifier(): returns True if the string is a valid Python identifier (variable name),otherwise it returns False.
print("isidentifier : ", a.isidentifier())
print("isidentifier : ", "12abc".isidentifier())

print("islower(): ",a.islower())
print("isupper(): ",a.isupper())
print("istitle(): ",a.istitle())
print("isspace(): ",a.isspace())

# isprintable() :returns True if all characters in the string are printable,otherwise False.
print("isprintable(): ",a.isprintable())

#replace(): replaces each matching occurrence of a substring with another string.
print("replace(old, new) : ",a.replace("l","L"))
print("replace(old, new, count) : ",a.replace("l","@@",2))

a="Hello World"
# split(separator, maxsplit):breaks down a string into a list of substrings using a chosen separator.
print("split(separator) : ",a.split())
print("split(separator, maxsplit) : ",a.split("l"))
print("split(separator, maxsplit) : ",a.split("l",2))

# rsplit(separator, maxsplit):breaks down a string into a list of substrings using a chosen separator,starting from the right.
print("rsplit(separator) : ",a.rsplit())
print("rsplit(separator, maxsplit) : ",a.rsplit("l"))

# partition(separator): splits a string into three parts: the part before the separator, the separator itself, and the part
print(a.partition("l"))
print("abc@gmail@.com".partition("@"))

# rpartition(separator): splits a string into three parts,starting from the right.
print("abc@gmail@.com".rpartition("@"))


# join(iterable): joins elements of an iterable (like a list or tuple) into a single string,using the string as a separator.
print("_python_".join("Python"))
print("$_".join("Python"))

# strip(chars): removes leading and trailing characters (default is whitespace) from a string.
print("      Python       ")
print("           Python       ".strip())
print("sPythonsss".strip('s'))

# lstrip(chars): removes leading characters (default is whitespace) from a string.
print("    Pythonsss".lstrip())
print("Pythonsss".lstrip("S"))

# rstrip(chars): removes trailing characters (default is whitespace) from a string.
print("Pythonsss      ".rstrip())
print("Pythonsss".rstrip("S"))

# rjust(width, fillchar): right-justifies a string within a specified width,using a fill character (default is space).
print("Python".rjust(20))
print("Python".rjust(20,'*'))
# ljust(width, fillchar): left-justifies a string within a specified width,using a fill character (default is space).
print("Python".ljust(20))
print("Python".ljust(20,'*'))

# zfill(width): pads a numeric string with zeros on the left,up to a specified width.
print("zfill(width):","python".zfill(20))

# translate(table): replaces characters in a string based on a translation table created by str.maketrans().
a="python"
b=str.maketrans('y','@')
print(b)
print(a.translate(b))
print(a)
b=a.maketrans('y','@','o')
print(b)
print(a.translate(b))
print(a.isprintable())

# expandtabs(tabsize): replaces tab characters with spaces,using a specified tab size.

a= "H\te\tl\tl\to"
print(a)
print("expandtabs(): ",a.expandtabs())
print("expandtabs(tabsize): ",a.expandtabs(2))
print("expandtabs(tabsize): ",a.expandtabs(4))
print("expandtabs(tabsize): ",a.expandtabs(10))



#encode(encoding, errors): encodes a string into bytes using a specified encoding and error handling scheme.
text = "pythón"
print(text.encode('utf-8'))  # Output: b'pyth\xc3\xb3'

print(text.encode('ascii'))  # Raises UnicodeEncodeError       


# Ignore non-ASCII
print(text.encode('ascii', errors='ignore'))  # b'pythn'

# Replace non-ASCII
print(text.encode('ascii', errors='replace'))  # b'pyth?n'

# 'xmlcharrefreplace' (replaces with XML character reference)
print(text.encode('ascii', errors='xmlcharrefreplace')) # b'pyth&#243;

# 'backslashreplace' (replaces with Python-style Unicode escape)
print(text.encode('ascii', errors='backslashreplace')) # Output: b'pyth\\xf3'

# 'namereplace' (Python 3.5+ — replaces with \N{...} names)
print(text.encode('ascii', errors='namereplace'))  # Output: b'pyth\\N{LATIN SMALL LETTER O WITH ACUTE}'