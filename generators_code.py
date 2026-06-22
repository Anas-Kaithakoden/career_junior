
# *yield,Generator functions

def count_to_five():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
for num in count_to_five():
    print(num)

# *Generator expressions
gen_exp = ( x ** 2 for x in range(1,6))
for num in gen_exp:
    print(num)

def even_number(limit):
    for num in range(2,limit+1,2):
        yield num
for n in even_number(10):
    print(n)