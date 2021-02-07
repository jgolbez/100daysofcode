'''
#List Comprehension = easy way to create new list from previous list
Format : new_list = [new_item for item in list]
'''
#Populate new list with doubling of numbers in current list
numlist = [1, 2, 3]
new_numbers = [num * 2 for num in numlist]
print(new_numbers)

#Same as above but now using a range instead of a list
range_numbers = [num * 2 for num in range(1, 4)]
print(range_numbers)


#works for strings also, in this case loops through each leter in a string and creates list
name = "Angela"
new_name_list = [letter for letter in name]
print(new_name_list)

'''
#Conditional List Comp
Format : new_list = [new_item for item in list if test]
'''
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

#Square Number List Comp
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

#Only Even Numbers in List
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]

