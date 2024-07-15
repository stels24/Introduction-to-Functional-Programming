def apply_all_func(int_list, *functions):
    reuslts = {}
    for i in functions:
        reuslts[i.__name__] = i(int_list)
    return reuslts


print(apply_all_func([6, 20, 15, 9], max, min, len, sum, sorted ))