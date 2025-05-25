# Write a Python program that:
# 1) while loop to repeatedly ask the user to enter a number as a string input.
# 2) Convert the input to an integer using typecasting.
# 3) If the input is not a valid number (e.g. "abc"), skip to the next iteration using a control
# statement.
# 4) If the number is negative, stop the loop using a control statement.
# 5) Otherwise, print the number with the message: "You entered: <number>".
# 6) program should continue until the user enters a negative number.
# (Hint: use break,continue control statement)

while True:
      num=int(input("Enter a number: "))
      if num < 0:
        print("Negative number entered. Exiting...")
        break
      else:
         print("You entered:",num)
         


# Write a Python program that:
# 1) Use while loop to ask the user to enter a number both real numbers (e.g., 5, 2.5) and complex
# numbers (e.g., 3+4j).
# 2) Use typecasting with complex() to convert the input.
# 3) If the input is invalid (e.g., "abc"), skip using a control statement.
# 4) If the real part is negative, stop the loop.
# 5) Otherwise, print the real and imaginary parts separately.
# 6) Count how many valid complex numbers were entered before stopping

count = 0
while True:
    num =complex(input("Enter a real or complex number: "))
    if num.real<0:
        print("Negative real part detected. Exiting...")
        break
    else:
        count += 1
    print("Real part:",num.real,"Imaginary part:", num.imag)

# Final output
print(f"Total valid complex numbers entered: {count}")




# Factorial Calculator with Input Validation .write a Python program that:
# 1. Repeatedly asks the user to enter a non-negative integer.
# 2. Use typecasting to convert the input to an integer.
# 3. If the input is invalid or negative, print "Invalid input. Please enter a non-negative integer." and
# ask again.
# 4. If valid, calculate and print the factorial of the number.
# 5. After showing the factorial, ask the user if they want to calculate another factorial (yes or no).
# 6. If the user enters "no", stop the program. If "yes", continue.

while True:
     num = int(input("Enter a non-negative integer: "))
     if num<0:
            print("Invalid input. Please enter a non-negative integer.")
            continue
     else:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i
        print("Factorial of", num, "is", factorial)

        
     again = input("Do you want to calculate another factorial? (yes/no): ")
     if again != "yes":
            print("Exit")
            break



#check given number is prime or not
flag =0
n=5
for i in range(2,n):
    if(n%i==0):
        flag=1
        break
print("not Prime")if flag==1 else print("prime")

# Write a Python program to print Fibonacci series
n = int(input("Enter the number of terms: "))
a, b = 0, 1
count = 0
print("Fibonacci sequence:")
#using a while loop
while count < n:
        print(a, end=' ')
        a, b = b, a + b
        count += 1 

#using for loop
for i in range(n):
    print(a, end=' ')   
    a, b = b, a + b


# write a Python program to Count vowels in a string using for loop 
str = input("Enter a string: ")
count = 0
vowels = "aeiouAEIOU"
for char in str:
    if char in vowels:
         count+= 1
print("Number of vowels:", count)

#  Given a number num = 100, print it in decimal, hexadecimal, octal, and binary formats,
# each with the appropriate prefix (0x, 0o, 0b).
num = 100
print("Decimal     :", num)
print("Hexadecimal :", hex(num))  
print("Octal       :", oct(num))
print("Binary      :", bin(num))  