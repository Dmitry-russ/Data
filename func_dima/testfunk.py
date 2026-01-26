
import functools

def dec(funk):
    def wrap():
        res = funk()
        print(type(res))
        return res
    return wrap

def dec_data(data):
    def dec(funk):
        def wrap():
            res = funk()
            print(type(res))
            print(data)
            return res
        return wrap
    return dec

@dec_data("test")
def test(str):
    print(str)


# test("Hello")


def repeat(n_times):
    """Декоратор, который повторяет вызов функции n раз."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(n_times):
                results.append(func(*args, **kwargs))
            return results
        return wrapper
    return decorator

# Использование:
@repeat(n_times=3)
def say_hello(name):
    return f"Hello, {name}!"

print(say_hello("Alice"))

# Обычная функция
def squares_list(n):
    result = []
    for i in range(n):
        result.append(i**2)
    return result  # возвращает весь список сразу

# Генератор
def squares_gen(n):
    for i in range(n):
        yield i**2  # возвращает по одному элементу

print(squares_list(2))
print(squares_gen(2))