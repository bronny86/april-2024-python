# string methods:
# len
# lower
# upper
# split
# join
# replace

# len = length of all characters in the string including spaces

name = "Minky Binky"

print(len(name))

# lower

print(name.lower())

# upper

print(name.upper())

# split

print(name.split())

print(name.split("n"))

# joined

splitted_name = name.split()

joined_name = " ".join(splitted_name)

print(joined_name)

# replace

print(name.replace ('i', 'a'))


