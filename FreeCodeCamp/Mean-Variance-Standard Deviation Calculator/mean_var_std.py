import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    arr = np.array(list).reshape((3,3))
    def stat(func):
        return [func(arr, axis=0).tolist(),
                func(arr, axis=1).tolist(),
                func(arr).tolist()]

    calculations = {
        'mean': stat(np.mean),
        'variance': stat(np.var),
        'standard deviation': stat(np.std),
        'max': stat(np.max),
        'min': stat(np.min),
        'sum': stat(np.sum)
    }

    print(calculations)
    return calculations