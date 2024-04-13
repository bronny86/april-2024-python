# non-primative data types 

# list - collection of data (not just one type of data), list of primative data types, list of non-primative data types, is mutable becuase we can change the data we have inside the list or change by adding/removing data in the list, list is indexed collection of data, represented by []

numbers = [ 12, 32, 2, 4, 56, 78 ]
# index      0   1  2  3   4   5

print(numbers)
print(numbers[4])

numbers.append(12)
print(numbers)

numbers[1] = 25 # indexed number 1 (32) changed to 25
print(numbers)

numbers.pop() # removes last number in list
print(numbers)

# Tupples - collection data, immutable not mutable (cannot be changed/edited), is indexed,  cannot add or remove or edit, Read Only data, # can have duplicated data in Tuple, represented by ()

days = ("Monday", "Tuesday", "Wednesday", "Tuesday" )
# index    0           1          2             3
print (days)
print(len(days)) #how mnay items in the tuple


# SETS - collection of data, similar to list - is mutable (can be changed), is not indexed so order doesn't matter, no repeated items, represented by {}, if try to add repeated items just will show once, if you have a list with duplicate items can change into a set to get rid of duplicates and then convert back into a list and duplicate items will be removed

names = {"Minky", "Bootsy", "Dan"}

print(names) # displays in random order because not indexed

names.add("Hooky") #not append because doesnt go at the end  because not indexed and will display in random order so add just adds wherever
print(names)

names.remove("Minky")
print(names)

# dictionary collection of data, mutable  (can be changed), keyed, key value pair, cannot index, keyed

person1 = {
    "name": "Minky", # name = key
    "surname": "Binky", # surname = key
    "age": 15 #age = key
}

print(person1)
print(person1["name"]) # calling the key name in []
print(person1.get("name"))

print(person1.get("phone", "No phone number provided")) #if calling a key that doesnt exist will print 'none'or can add a statement to display if doesnt exist 'no phone number')

person1["address"] = "Richmond"  #adding new key/new data
print(person1)

person1["age"] = 1 #change data in existing key
print(person1)

person1.pop("surname") #remove key
print(person1)

# Loop

print("Loop started here: /n")

for key in person1:
    print(f"Key: {key}")
    print(f"Value: {person1[key]}")

