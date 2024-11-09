# Create a set using curly braces (this will automatically remove duplicates)
from enum import unique

my_set = {1, 1, 2, 3, 3, 4, 5, 3, 2, 3}
print("Set after duplicates removed:", my_set)

# Define two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union method
union_method = set1.union(set2)

# Union using the | operator
union_operator = set1 | set2

print("Union of set1 and set2 using method:", union_method)
print("Union of set1 and set2 using operator:", union_operator)

# Intersection method (fixed typo from 'intersetion' to 'intersection')
intersection_method = set1.intersection(set2)

# Intersection using the & operator
intersection_operator = set1 & set2

print("Intersection of set1 and set2 using the intersection method:", intersection_method)
print("Intersection of set1 and set2 using the & operator:", intersection_operator)

# Difference method
difference_method = set1.difference(set2)

# Difference using the - operator
difference_operator = set1 - set2

print("Difference of set1 and set2 using the difference method:", difference_method)
print("Difference of set1 and set2 using the - operator:", difference_operator)

# Symmetric difference method
symmetric_difference_method = set1.symmetric_difference(set2)

# Symmetric difference using the ^ operator
symmetric_difference_operator = set1 ^ set2

print("Symmetric difference of set1 and set2 using symmetric difference method:", symmetric_difference_method)
print("Symmetric difference of set1 and set2 using ^ operator:", symmetric_difference_operator)

# Working with set modifications
my_set = {1, 2, 3}

# Adding an element
my_set.add(7)

# Removing an element (raises KeyError if the element is not found)
my_set.remove(3)

# Discarding an element (does not raise error if the element is not found)
my_set.discard(8)

print("Set after adding, removing, and discarding:", my_set)

# Clearing the set
my_set.clear()
print("Set after clearing:", my_set)

my_list = [1,2,2,2,3,4,4,4,5,6]

#Convert this list to a set ton remove duplication
uniqe_set=set(my_list)

print(uniqe_set)

unique_list = list(uniqe_set)
print(unique_list)

blertas_interest = {"music,""movies,""travel"}
drilonis_interest = {"movie,""games,""skiing"}

common_intrests = blertas_intrests.intrestsion(drilonis_intrests)
print(common_intrests)

colors = {"red","blue"}
color