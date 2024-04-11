# find the highest number

# take input from user three numbers a, b, c
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# If a > b?

if a > b:
    #if a > c
    if  a > c:
        #display a
        print(a)
            # else print C
    else:
        print(c)

# ELSE 
else:
    # then is b > c
    if b > c:
        print(b)
        # if yes print B
    else:
        print(c)
        # else print C