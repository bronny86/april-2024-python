# five log in attempts allowed
# example of while loop

login_attempts = 5
actual_password = "hello"

while login_attempts > 0:
    password = input("Enter password: ")
    if (password != actual_password):
        print ("Wrong password")
        login_attempts -= 1
        print(f"Remaining attempts: {login_attempts}")
        if (login_attempts == 0):
            print("You have run out of attempts")
    else:
        print("Login successful")
        break
