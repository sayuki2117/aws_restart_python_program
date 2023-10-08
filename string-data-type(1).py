print("==========Exercise 1 Introducing the string data type=========\n")
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
print("==========Exercise 2 string concatenation==========\n")
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)
print("=========Exercise 3: Working with input strings==========\n")
name = input("What is your name? ")
print(name)
print("==========Exercise 4: Formatting output strings===========\n")
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))