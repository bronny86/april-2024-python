# find sum of all the multiples of 3 or 5 below 1000

def sum_of_multiples():
    sum = 0
    #Iterate from 1 to 1000
    for i in range(1, 1000):
    #  if multiple of 3 or 5
        if (i % 3  == 0 or i % 5 == 0):
        # add that to the variable 'sum'
            sum += i
            # return sum
    return sum

final_sum = sum_of_multiples()
print(final_sum)
