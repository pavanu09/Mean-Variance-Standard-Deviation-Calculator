import numpy as np


def calculate(nums):
    if len(nums) != 9:
        raise ValueError("List must contain nine numbers.")
    array = np.array(nums)
    array = array.reshape((3, 3))
    calculations = {
        'mean': [array.mean(axis=0), array.mean(axis=1), array.mean()],
        'variance': [array.var(axis=0), array.var(axis=1), array.var()],
        'standard deviation': [
            array.std(axis=0), array.std(axis=1), array.std()],
        'max': [array.max(axis=0), array.max(axis=1), array.max()],
        'min': [array.min(axis=0), array.min(axis=1), array.min()],
        'sum': [array.sum(axis=0), array.sum(axis=1), array.sum()]
    }
    return calculations
