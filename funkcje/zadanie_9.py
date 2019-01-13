import time
# funkcja time mierzy sekundy od Epoch time czyli chyba od 1 stycznia 1970

start = time.time()
lista = [x*2 for x in range(1000000)]
stop = time.time()

print(stop-start)

def baz():
    pass

def foo(bar):
    print(bar.__name__)

foo(baz)

#zadanie 9
print("zadanie9")

def log(funkcja):
    def wrapper(*args, **kwargs):
        start=time.time()
        result = funkcja(*args, **kwargs)
        stop = time.time()
        duration = stop - start
        print(f'Długość wywołania {funkcja.__name__} to {duration} s')
        return result
    return wrapper

@log
def foo(arg):
    return f'To jest {arg}'

print("-"*40)
foo("1")
wynik = foo('1')
print(wynik)

"""
Do mierzenia czasu w ipython jest metoda %timeit -n1
"""

# def test_decorated_foo():
#     assert foo(1) == "Długość wywołania foo" in foo(1)