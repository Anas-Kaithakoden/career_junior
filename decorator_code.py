def decorator(func):

    def wrapper():
        print("Running function...")
        func()

    return wrapper

@decorator
def greet():
    print("Hello")

greet()


def decorator(func):

    def wrapper():
        func()
        print("Finished")

    return wrapper

@decorator
def greet():
    print("Hello")

greet()


def decorator(func):

    def wrapper():
        print("Starting...")
        func()
        print("Done!")

    return wrapper

@decorator
def say_name():
    print("Anas")

say_name()


