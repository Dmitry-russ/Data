def move_zeros(data):
    res: list = []
    nul_number = data.count(0)
    res = [x for x in data if x != 0]
    if nul_number:
        _ = [res.append(0) for i in range(nul_number)]
    print(res)





move_zeros([0, 8, 9, 0, 1, 2, 0])  # [8, 9, 1, 2, 0, 0, 0]
move_zeros([1, 2, 3]) 