def square(number: int) -> int:
    return number ** 2

def full_name(first: str, last: str) -> str:
    return f"{first} {last}"

def get_total(numbers: list[int]) ->  int:
    return sum(numbers)

def get_user() -> dict[str, str | int]:
    return {"name": "anas", "age": 21}

def withdraw(balance: int, amount: int) -> int:
    if amount > balance:
        raise ValueError("Insufficenit Funds")
    return balance - amount