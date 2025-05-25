#Simple pattern printing using while loop
i =0
while i<4:
    j=0
    while j<4:
        print('*',end="")
        j += 1
    print()
    i = i + 1

#Program to print half pyramid using while loop
i =0
while i < 4:
    j = 0
    while j<i :
        print('*',end="")
        j += 1
    print()
    i = i + 1

#Program to print half pyramid using for loop
rows=3
for i in range(rows):
    for j in range(i+1):
        print("*", end="")
    print()