import numpy as np


def do_it(func, *args):
    axis1 = func(*args, axis=0)
    list1 = axis1.tolist()
    axis2 = func(*args, axis=1)
    list2 = axis2.tolist()
    flattened = func(*args)
    return [list1, list2, flattened]


def calculate(lista):
    if not isinstance(lista, list) or (isinstance(lista, list)
                                       and len(lista) != 9):
        raise ValueError('List must contain nine numbers.')

    arr = np.reshape(lista, (3, 3))
    calculations = {}

    calculations['mean'] = do_it(np.mean, arr)
    calculations['variance'] = do_it(np.var, arr)
    calculations['standard deviation'] = do_it(np.std, arr)
    calculations['max'] = do_it(np.max, arr)
    calculations['min'] = do_it(np.min, arr)
    calculations['sum'] = do_it(np.sum, arr)

    return calculations


def calculate_old(lista):
    if not isinstance(lista, list) or (isinstance(lista, list)
                                       and len(lista) != 9):
        raise ValueError('List must contain nine numbers.')

    arr = np.reshape(lista, (3, 3))
    calculations = {}

    axis1 = arr.mean(axis=0).tolist()
    axis2 = arr.mean(axis=1).tolist()
    flattened = arr.mean()
    calculations['mean'] = [axis1, axis2, flattened]

    axis2 = arr.var(axis=1).tolist()
    flattened = arr.var()
    calculations['variance'] = [axis1, axis2, flattened]

    axis1 = arr.std(axis=0).tolist()
    axis2 = arr.std(axis=1).tolist()
    flattened = arr.std()
    calculations['standard deviation'] = [axis1, axis2, flattened]

    axis1 = arr.max(axis=0).tolist()
    axis2 = arr.max(axis=1).tolist()
    flattened = arr.max()
    calculations['max'] = [axis1, axis2, flattened]

    axis1 = arr.min(axis=0).tolist()
    axis2 = arr.min(axis=1).tolist()
    flattened = arr.min()
    calculations['min'] = [axis1, axis2, flattened]

    axis1 = arr.sum(axis=0).tolist()
    axis2 = arr.sum(axis=1).tolist()
    flattened = arr.sum()
    calculations['sum'] = [axis1, axis2, flattened]

    return calculations
