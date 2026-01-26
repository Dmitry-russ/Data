import datetime

def counter(limit):
    print("Генератор ЗАПУЩЕН")
    count = 0
    while count < limit:
        print(f"До yield: count = {count}")
        yield count  # <-- ПАУЗА! Возвращаем count и "засыпаем"
        print(f"После yield")
        count += 1
    print("Генератор ЗАВЕРШЕН")

# Создаем генератор
gen = counter(3)
value1 = next(gen)  # Выведет: "Генератор ЗАПУЩЕН" и "До yield: count = 0"
value2 = next(gen)  # Выведет: "После yield" и "До yield: count = 1"
value3 = next(gen)  # Выведет: "После yield" и "До yield: count = 2"

print("\nЧетвертый next():")
try:
    value4 = next(gen)  # Выведет: "После yield" и "Генератор ЗАВЕРШЕН"
except StopIteration:
    print("Генератор закончился!")

# список квадратов четных чисел:
def kvadrat(limit):
    res = [n*n for n in range(limit)]
    return print(res)

kvadrat(11)

data = [('a', 1), ('b', 2), ('a', 3), ('c', 4), ('b', 5)]
def sum(data):
    resul = {}
    for dat in data:
        if dat[0] in resul:
            resul[dat[0]] = resul[dat[0]] + dat[1]
        else:
            resul[dat[0]] = dat[1]
    return print(resul)

sum(data)

def timer(func):
    def wrap(*args, **kwargs):
        date = datetime.now()
        res = func(*args, **kwargs)
        date_2 = datetime.now()
        time = date_2 - date
        print(time)
        return res
    return wrap
