
# *Parameters, Return values -------

def say_hello(name):
    print(f"Hello {name}")
say_hello("anas")

def square(a):
    return a ** 2
print(square(7))

def is_even(num):
    return True if num % 2 == 0 else False
print(is_even(2))

def full_name(first, last):
    return f"{first} {last}"
print(full_name("anas", "kk"))

def calculate_area(leng, wid):
    return leng * wid
print(calculate_area(4,3))

def cal_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
    
print(cal_grade(75))


# *Scope -----

def increase(num):
    return num + 1

print(increase(6))

def deposit(balance, amount):
        return balance + amount

print(deposit(1000, 300))

def withdraw(balance, amount):
      return balance - amount if amount < balance else "Insufficient funds"

print(withdraw(800, 600))


# *Default Arguments ------

def power(number, exponent=2):
    return number ** exponent

print(power(2, 3))

def create_account(username, role="user"):
    return f"Username: {username} Role: {role}"

print(create_account("anas"))

def calculate_price(amount, tax =0.18):
    return amount + (amount * tax)

print(calculate_price(100))


# *args -------
def show_names(*args):
    for name in args:
        print(name)
show_names("anas", "kk", "sanu")

def multiply(*args):
    product = 1
    for num in args:
        product = product * num
    return product

print(multiply(3,5,6))

def find_max(*args):
    biggest = args[0]
    for num in args:
        if num > biggest:
            biggest = num
    return biggest
print(find_max(7,10,15,3,27,1))

# **kwargs -------
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
show_details(name="anas", age=21)

