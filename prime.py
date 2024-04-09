## check if a number is prime or not - only divided by itself and 1

def is_prime(number): #10
    for i in range(2, number): # 2 to 9
        if (number % i ==0):
            print("Not a prime")
            break
    else:
        print("Prime")

is_prime(10)
is_prime(3)