
# *try,except,else,finally

def safe_division(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Cannot divide by Zero"

print(safe_division(9,0))

def safe_get(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Invalid Index"
    
lst = [3,6,9]
print(safe_get(lst, 2))

def safe_int(num):
    try:
        return int(num)
    except ValueError:
        return "inavlid number"
    
def testing_new(num):
    try:
         print(int(num))
    except ValueError:
         print("inavlid number")
    else:
        print("success")
    finally:
        print("worked")

testing_new("abc")    
    

# *Raising Exceptions

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        return age

print(validate_age(21))

def validate_password(password):
    if len(password) < 8:
        raise ValueError("Password must be atleast 8 characters")
    else:
        return password
print(validate_password("anaskkttpp"))

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")
    else:
        return balance - amount
    
try:
    print(withdraw(1000, 1200))
except ValueError as e:
    print(e)