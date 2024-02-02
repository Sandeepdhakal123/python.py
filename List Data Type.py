"""
List data type.
  => List data type is the type if data type which is changable or you can modify it is called list 
  ** Use of the list data type 
  List data type is used to store a collections of items which is defined using
  Square brackets []
"""

#Example of list type

# Creating list in numbers

numbers = [1, 2, 3, 4, 5, 6, 7]

#Creating list in string

name_of_cities = ["Ogden", "Kathmandu", "Newyork"]

#Creating the mixed-type list

mixed_list = [1, "apple", 3.14, True, "grapes"]

print(numbers[5])          #the output is 5

print(name_of_cities[2]) #the output is Newyork

print(mixed_list) # the outpu is [1, 'apple', 3.14, True, 'word']

#Modifying the elements in the numbers / Adding elements in the list

numbers[0]= 17
print (numbers)

# Adding elements in the list     ( Always remember that in python "append" is always add the elements.)

numbers.append(8)
print(numbers)

# Removing Elements in the list (Remove function is alwasyys used to eliminate the objects from the list )
mixed_list.remove("apple")
print(mixed_list)
#Finding the length of the list
print(len(name_of_cities))
