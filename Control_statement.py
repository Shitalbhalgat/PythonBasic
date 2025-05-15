#if statement syntax
# if (condition):
#     print("statement 1")
# print("statement 2")   

#write a python program to take Selling Price and Cost Price from user and check if the shopkeeper get a profit or loss and print amt after profit and loss
a=int(input("Enter Selling Price"))
b=int(input("Enter Cost Price")) 
if (a>b):
    print("profit")
    print(a-b)
if (a<b):
   print("loss")    
   print(a-b)

#write a python program to entered number is in between 1500 to 2100 if yes then print given no is between the condition
a=int(input("Enter a number"))
if a>=1500 and  a<=2100:
    print("Yes the number is between given range")

# write a python program to calculate absolute value:
a=int(input("enter a value :"))
if a<0 :
    print(-a)

#if else statement syntax
# if (condition):
#     print("statement 1")
# else:   
#     print("statement 2")   

#write a python program to check candidate are eligible for vote or not
a=int(input("enter age :"))
if(a>=18) :
    print("you are eligible")
else:
    print("you are not eligible")

#write a python program to check shape given is rectangle or square
l=int(input("enter length :"))
b=int(input("enter breath :"))
if l==b:
    print("It is a square")
else:
    print("It is a rectangle")

#write a python program to check enter year is leap or not
a=int(input("enter year:"))
if a%400==0 or (a%4==0 and a%100!=0):
   print("It is a leap year")
else:
     print("It is not a leap year") 

#elif statement/elif ladder:
#if the condition is true then if block will execute otherwise next elif block will check for condition if the cond is true elif block will execute or else block will execute
#note: in elif ladder many elif blocks and single else block

#syntax of elif:
# if():
#     print()
# elif():
#     print()
# elif():
#     print()
# else:
#     print()

#example
if(True):
    print("if")
elif(True):
    print("elif1")
elif(True):
    print("elif2")
else:
    print("else")
     

