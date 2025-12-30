from algoritm import call_func


# --- стр. 96 задача 1 (функция для суммы значений в списке)
def rec_sum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        element = arr.pop(0)
        return element + rec_sum(arr)


# test_data = [5, 8, 9, 4, 45, 2, 12, 22, 33, 1, 5, 200]
# call_func(test_data, rec_sum)


# ---- стр. 96 задача 2 (подсчет количества в списке)
def rec_count(arr):
    if arr == []:
        return 0
    else:
        arr.pop(0)
        return 1 + rec_count(arr)


# test_data = [5, 8, 9, 4, 45, 2, 12, 22, 33, 1, 5, 200, 5, 6, 8, 4]
# call_func(test_data, rec_count)


# ---- стр. 96 задача 3 (наибольшее числов списке)
def rec_max(arr):
    if len(arr) == 1:
        return arr.pop(0)
    else:
        max_element_1 = arr.pop(0)
        max_element_2 = rec_max(arr)
        if max_element_1 >= max_element_2:
            return max_element_1
        else:
            return max_element_2


test_data = [5, 8, 9, 4, 45, 2, 12, 22, 330, 1, 5, 200, 5, 6, 8, 4]
call_func(test_data, rec_max)
