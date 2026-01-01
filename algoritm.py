import time


def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"\n{func.__name__} выполнилась за {elapsed_time:.6f} секунд")
        return result
    return wrapper


def findesmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


@log_execution_time
def selectionsort(arr):
    newarr = []
    copiedarr = list(arr)
    for i in range(len(copiedarr)):
        smallest = findesmallest(copiedarr)
        newarr.append(copiedarr.pop(smallest))
    return newarr


@log_execution_time
def call_func(arr, func):
    print(func(arr))


# test_data = [5, 8, 9, 4, 45, 2, 12, 22, 33, 1]
# print(selectionsort(test_data))

# sorted = log_execution_time(sorted)
# print(sorted(test_data))


def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)


# @log_execution_time
# def call_func(i):
#     countdown(i)


# call_func(997)

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


# @log_execution_time
# def call_func(x):
#     print(fact(x))


# call_func(5)


# стр. 96 задача 1 (функция для суммы значений в списке)
def rec_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        element = arr.pop(0)
        return element + rec_sum(arr)


# test_data = [5, 8, 9, 4, 45, 2, 12, 22, 33, 1, 5, 200]
# call_func(test_data, rec_sum)

# стр. 96 задача 1 (функция для суммы значений в списке)

# проверяю кк назначаются переменные в python
test = [1, 2]
tset2 = test
test.append(3)
print(test)
print(tset2)
tset2.append(4)
print(test)
print(tset2)

str_test = "test"
str_test2 = str_test
str_test += "1"
print(str_test)
print(str_test2)
