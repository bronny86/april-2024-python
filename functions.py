# Function is a collection of code that performs a single task
# starts with 'def' keyword followed  by name of the function
# optional - then list of arguments (inputs to the function) go inside ()
# then the lines of code that the function will represent
# optional - return statement (output of function)


#declaring the function
def greet():
    print ("Hello World!!")

#calling the function
greet()

#adding arguments
def greet(fname, lname):
    print(f"Hello {fname} {lname}")

greet("Steven", "Smith")

