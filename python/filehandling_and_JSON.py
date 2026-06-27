import json

user = {
    "name": "Anas",
    "age": 21
}
with open("users.json", "w") as file:
    json.dump(user, file)
with open("users.json", "r") as file:
    content = json.load(file)
print(content["name"])



name = input("what is your name: ")
age = input("what is your age: ")
data = {"name": name, "age": age}

with open("users_new.json", "w") as file:
    json.dump(data, file, indent=4)

with open("users.json", "r") as file:
    content = json.load(file)

print(f'Welcome {content["name"]}, age: {content["age"]}')

