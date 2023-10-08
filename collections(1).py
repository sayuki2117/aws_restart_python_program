print("==========Exercise 1: Introducing the list data type==========\n")
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# Accessing a list by position
print("==========Accessing a list by position=========")

# To access the banana string, enter the following:
print(myFruitList[0])
#To access the cherry string, enter the following code:
print(myFruitList[1])
# To access the cherry string, enter the following code:
print(myFruitList[2])
# Changing the values in a list
print("==========Changing the values in a list==========")
myFruitList[2] = "orange"
print(myFruitList)
print("\n")
print("==========Exercise 2: Introducing the tuple data type==========")

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
# Accessing a tuple by position
print("==========Accessing a tuple by position==========")
# To access the apple string, enter the following code:
print(myFinalAnswerTuple[0])
# To access the banana string, enter the following code:
print(myFinalAnswerTuple[1])
# To access the pineapple string, enter the following code
print(myFinalAnswerTuple[2])
print("\n")
print("==========Exercise 3: Introducing the dictionary data type==========")
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print("==========Accessing a dictionary by name==========")

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])
