def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        less = []
        more = []
        mid = arr[0]  # бере произвольное число из массива как опорное
        for i in arr[1:]:
            if i <= mid:
                less.append(i)
        for i in arr[1:]:
            if i > mid:
                more.append(i)
        return quick_sort(less) + [mid] + quick_sort(more)


arr = [5, 8, 9, 4, 45, 2, 12, 22, 33, 1]
print(quick_sort(arr))
