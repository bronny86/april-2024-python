#scope - global and local
# local variable only availablee within that function
# global variables available anywhere in the code

fname = "Minky"
lname = "Binky"

def greet():
    fname = "Booey"
    lname = "Gooey"
    print("Inside the function LOCAL")
    print(fname)
    print(lname)

greet()

print("Outside the function GLOBAL")
print(fname)
print(lname)


