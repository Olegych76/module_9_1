def apply_all_func(int_list, *functions):
    results = dict()
    for func in functions:
        results[func.__name__] = func(int_list)
    return results  # возвращает словарь с результатами функций


def min_(int_list):  # принимает список, возвращает минимальное значение из него
    min_num = int_list[0]
    for num in int_list:
        if num < min_num:
            min_num = num
    return min_num


def max_(int_list):  # принимает список, возвращает максимальное значение из него
    max_num = int_list[0]
    for num in int_list:
        if num > max_num:
            max_num = num
    return max_num


def len_(int_list):  # принимает список, возвращает кол-во элементов в нём
    return len(int_list)


def sum_(int_list):  # принимает список, возвращает сумму его элементов
    return sum(int_list)


def sorted_(int_list):  # принимает список, возвращает новый отсортированный список на основе переданного
    return sorted(int_list)


print(apply_all_func([6, 20, 15, 9], max_, min_))
print(apply_all_func([6, 20, 15, 9], len_, sum_, sorted_))
