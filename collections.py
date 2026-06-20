
# *Lists,Tuples,Dictionaries,Sets


def get_total(lst):
    total = 0
    for num in lst:
        total += num
    return total
print(get_total([1,5,6]))

def remove_duplicates(lst):
    dummy_set = set()
    new_list = []
    for num in lst:
        dummy_set.add(num)
    for num in dummy_set:
        new_list.append(num)
    return new_list

print(remove_duplicates([7,8,4,7,3,1,1,6,4,8,2]))

def get_user_info(user):
    return f'{user["name"]} is {user["age"]} years old and lives in {user["city"]}'

print(get_user_info({ "name": "anas", "age": 21, "city": "mlp"}))


# *List Comprehensions

# 3: 
nums =  [n ** 2 for n in [1,2,3,4,5]]
print(nums)

# 4:
names = [name.upper() for name in ["anas","ali","john"]]
print(names)

# 5:
only_odd = [num for num in [1,2,3,4,5,6,7,8,9] if num % 2 != 0]
print(only_odd)

# Challenge:
active_users = [user["name"] for user in [{"name": "anas", "active": True},{"name": "ali", "active": False}, {"name": "john", "active": True}] if user["active"]]
print(active_users)


#  *Dictionary Comprehensions

# 2:
squares = {
    n: n **2
    for n in [1,2,3,4]
}
print(squares)

# 3:
name_length = {
    name: len(name)
    for name in ["anas", "ali", "john"]
}
print(name_length)

# Challenge:
even_squares = {
    n: n ** 2
    for n in [1,2,3,4,5,6]
    if n % 2 == 0
}
print(even_squares)