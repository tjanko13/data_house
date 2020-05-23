def mean(x):
    x_mean = sum(x) / len(x)
    return x_mean


def error(n, lst):
    lst = list(lst)
    error_lst = []
    for i in lst:
        num = (i - n)
        error_lst.append(num)
    return error_lst

# import numpy as np
# def mean(lst):
#    mean_of_list = np.mean(lst)
#    return mean_of_list
