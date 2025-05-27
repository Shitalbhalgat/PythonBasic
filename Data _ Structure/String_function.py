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


# print(a.split("'ß'"))
# print(a.split("l"))
# print(a.split("l",2))
# print(a.partition("l"))
# print("abc@gmail@.com".partition("@"))
# print("abc@gmail@.com".rpartition("@")

print("Shital".rjust(20))
print("Shital".rjust(20,'*'))
print("Shital".ljust(20))
print("Shital".ljust(20,'*'))
print("      Shital       ")
print("           Shital       ".strip())
print("ShiStalS".strip('S'))
print("    ShiStalS".lstrip())
print("ShiStalS".lstrip("S"))
print("ShiStalS      ".rstrip())
print("ShiStalS".rstrip("S"))
print("_python_".join("Shital"))
print("python".zfill(20))
a="python"
b=str.maketrans('y','@')
print(b)
print(a.translate(b))
print(a)
b=a.maketrans('y','@','o')
print(b)
print(a.translate(b))
print(a.isprintable())

# print("Ståle".encode(encoding="ascii",errors="replace"))
# print(b.encode(encoding="ascii",errors="replace"))
# print(b.encode(encoding="ascii",errors="backslashreplace"))

a= "H\te\tl\tl\to"
print(a)
print("expandtabs(): ",a.expandtabs())
print("expandtabs(tabsize): ",a.expandtabs(2))
print("expandtabs(tabsize): ",a.expandtabs(4))
print("expandtabs(tabsize): ",a.expandtabs(10))