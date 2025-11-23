#Unordered: You won’t know the order of elements.
#Mutable: You can change the set’s contents by adding or removing items.
#Unique: Sets automatically remove duplicate items.
#No Indexing: Unlike lists or tuples, sets don't have a defined order, 
# so you can't access items using an index.

#To create an empty set, we use the set() function because {} is used for dictionaries.
#We can create a set by listing its values inside curly braces. Remember, 
# sets automatically remove any duplicate values

#Working with Lists, Tuples, and Dictionaries
#Sets are also great for removing duplicates from other data structures. 
# For example, you can convert a list into a set to eliminate duplicate values:
#Practice

unique_flowers = {'dahlia', 'sunflower', 'black rose'}
with open('unique_flowers.txt','w') as file:
    for flower in unique_flowers:
        file.write(flower + '\n')    
my_set = {'dahlia', 'sunflower', 'black rose'}
print('black rose' in my_set)  # Output: True
print('tulip' in my_set)      # Output: False

#The 'in' keyword: Is your friend at the party?
...
guests = {'Alice', 'Bob', 'Charlie'}
if 'Alice' in guests:
    print("Alice is here!")
else:
    print("Alice is not here.")

my_set = {'superman', 'batman', 'wonder woman'}
my_set.add('green lantern')
print(my_set)  # Output: {'superman', 'batman', 'wonder woman', 'the flash', 'green lantern'}

foods = {'pizza', 'burger', 'pasta', 'ice cream'}
foods.add('cannoli')  # Adding a new item
print('pasta' in foods)  # Checking for an item
print(foods)

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print(set1.issubset(set2))  # Output: True
print(set2.issuperset(set1))  # Output: True

set1 = {'basketball', 'soccer', 'tennis'}
set2 = {'basketball', 'soccer'}

print(set2.issubset(set1))  # Is set2 a subset of set1?
print(set1.issuperset(set2))  # Is set1 a superset of set2?

...
#Union: The Grand Gathering
...

set1 = {'Alice', 'Bob', 'Charlie'}
set2 = {'David', 'Emma', 'Charlie'}
grand_gathering = set1.union(set2)
print(grand_gathering)  # Output: {'Alice', 'Bob', 'Charlie', 'David', 'Emma'}

#Intersection: The Common Ground
set1 = {'Alice', 'Bob', 'Charlie'}
set2 = {'David', 'Emma', 'Charlie'}
common_guests = set1.intersection(set2)
print(common_guests)  # Output: {'Charlie'}

#Difference: The Exclusive Aspect Club
set1 = {'Alice', 'Bob', 'Charlie'}
set2 = {'David', 'Emma', 'Charlie'}
exclusive_guests = set1.difference(set2)
print(exclusive_guests)  # Output: {'Alice', 'Bob'}

#Symmetric Difference: The Unique Guests
set1 = {'Alice', 'Bob', 'Charlie'}
set2 = {'David', 'Emma', 'Charlie'}
unique_guests = set1.symmetric_difference(set2)
print(unique_guests)  # Output: {'Alice', 'Bob', 'David', 'Emma'}

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6}

# Intersection
print(set1.intersection(set2))  # Output: {3, 4}

# Difference
print(set1.difference(set2))  # Output: {1, 2}

# Symmetric Difference
print(set1.symmetric_difference(set2))  # Output: {1, 2, 5, 6}

set1 = {'Paris', 'Tokyo', 'New York'}
set2 = {'London', 'Paris', 'Rome'}

# Union
print("All unique destinations:", set1.union(set2))

# Intersection
print("Common destinations:", set1.intersection(set2))

# Difference
print("Destinations only in set1:", set1.difference(set2))

def clean_email_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    
    # Remove duplicates and merge
    all_unique = set1.union(set2)
    print("All unique emails:", all_unique)
    
    # Common emails
    common_emails = set1.intersection(set2)
    print("Emails in both lists:", common_emails)
    
    # Emails unique to each list
    unique_emails = set1.symmetric_difference(set2)
    print("Emails unique to each list:", unique_emails)

email_list1 = ['a@example.com', 'b@example.com', 'a@example.com']
email_list2 = ['b@example.com', 'c@example.com', 'd@example.com']

clean_email_lists(email_list1, email_list2)