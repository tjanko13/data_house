def mean(data: list) -> float:
    """Returns the mean of a list
    :param data: list of numeric values
    :return: float"""

    data_mean = sum(data) / len(data)
    return data_mean


def variance(data: list) -> float:
    """Variance of list
    :param data: list
    :return: float
    """

    data_mean = mean(data)
    ss = sum((i - data_mean)**2 for i in data)
    return ss


def std_dev(data: list, deg_of_freedom: int = 1) -> float:
    """Standard Deviation
    :param: data: list of numeric values
    param: dof:
    return: float
    """
    ss = variance(data)
    pvar = ss / (len(data) - deg_of_freedom)
    sd = pvar ** 0.5
    return sd


def covariance(data_x: list, data_y: list) -> float:
    """Calculates covariance btwn two data lists of numeric variavbles
    par: data_x list
    param data_y: list
    return: covariance float
    """
    covar = 0.0
    x_mean = mean(data_x)
    y_mean = mean(data_y)
    for i in range(len(data_x)):
        covar += (data_x[i] - x_mean) * (data_y[i] - y_mean)
    return covar
