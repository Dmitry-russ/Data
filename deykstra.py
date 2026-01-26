
def deykstra():
    pass

graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

# print(graph.get('start').get('a'))

s = 'dima'
s2 = s
s = s + '1'
print(s)
print(s2)

s = [1, 2]
s2 = s
s.append(3)
print(s)
print(s2)

nums = [n for n in range(1, 10)]
res = [n*n if i % 3 == 0 else n for n, i in enumerate(nums)]
print(res)

from func_dima.testfunk import test

test_str = "123"
test(test_str)


def my_decorator(func):
    def wrap(*arg, **kwarg):
        res = func()
        print(type(res))
        return res
    return wrap


@my_decorator
def f():
    return 10

f()
