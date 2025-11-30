a = 5
print("type of a:",type(a))

b = 2.5
print("type of b:",type(b))

c = "coding"
print("type of c:",type(c))

d = True
print("type of d:",type(d))


# Assigning Different Variables
name = "Penguin"
age = 15
is_student = True
weight = 38.5

# Printing Different Variables and their Data Type
print("Name: ", name)
print ("Data Type of Name is:",type(age) )

print("is_student:", is_student)
print("Data Type of is_student is", type(is_student))

print("Weight :",weight)
print("Data Type of weight is",type(weight))

# Type casting to convert the datatype of variables
print("\n After Type Casting ...")
age = str(age)
print(age)
print ("Data Type of age is", type(age))
weight = int(weight) 
print(weight)
print("Data Type of weight is", type(weight))

#input a word
text = str(input("Enter a string:"))
# Reverse String
# using step value as -1 to iterate in reverse
revText = text[::-1]
text = revText

print("Reverse of given string is:")
print(text)


Str = "beepboop"
print(Str[::3])
print(Str[0::1])
print(Str[::-1])