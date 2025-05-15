#Addition operator
a = 20
b = 10
print ("a + b : ", a + b)
print ("a - b : ", a - b)
print ("a * b : ", a * b)
print ("a / b : ", a / b)
print ("a % b : ", a % b)
print ("a ** b : ", a ** b)
print ("a // b : ", a // b)

#comparsion operators
a = 4
b = 5
print ("a == b : ", a == b)
print ("a != b : ", a != b)
print ("a > b : ", a > b)
print ("a < b : ", a < b)
print ("a >= b : ", a >= b)
print ("a <= b : ", a <= b)


# Assignment Operator
a=10
a += 5
print ("a += 5 : ", a)
a -= 5
print ("a -= 5 : ", a)
a *= 5
print ("a *= 5 : ", a)
a /= 5
print ("a /= 5 : ",a)
a %= 3
print ("a %= 3 : ", a)
a **= 2
print ("a **= 2 : ", a)
a //= 3
print ("a //= 3 : ", a)

#Logical Operator
a = True
b = False
print(a and b)
print(a or b)
print(not a)

#identity operator
a=5
b=5
print("a is b =",(a is b))
print("a is not b=",(a is not b))
a=[1,2,3]
b=[1,2,3]
print("a is b=",(a is b))
print("a is not b=",(a is not b))
a=(1,2,3)
b=(1,2,3)
print("a is b=",(a is b))
print("a is not b=",(a is not b))

#Membership operator
a="hello world"
print("h in a: ",('h' in a))
a=[1,2,3,5,6,4,8,9,7]
b=[1,2,3]
print("1 in a : ",(1 in a))
print("a in b: ",(a in b))
print("b in a : ",(b in a))
print("a not in b : ",(a not in b))
a=(1,2,3)
b=(1,2,3)
print("a in b : ",(a in b))
print("a not in b :",(a not in b))