from basics2 import mean, variance, covariance


def fit_single_linear_regression(x: list, y: list) -> dict:
    """
    Fits a single linear regression in the format y = mx+b
    :param x: list
    :param y: list target
    :return: dict
    """
    m = covariance(data_x=x, data_y=y) / variance(data=x)
    b = mean(y) - m * mean(x)
    coefficients = {'m': m, 'b': b}
    return coefficients


def predict_single_linear_regression(x: list, model) -> list:
    """
    Utilizes lodel format y = mx +b where we are given predictors
    :param x: list of pred
    :param model: dict results
    :return:
    """
    predicted_y = [model['m'] * i + model['b'] for i in x]
    return predicted_y
