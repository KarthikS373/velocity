import numpy as np
import typing as tp


def is_sorted(a: tp.Array1d) -> np.bool_:
    """
    Check if array is sorted

    Parameters:
    a (array): The input array to be checked

    Returns:
    bool: True if the array is sorted, False otherwise
    """

    return np.all(a[:-1] <= a[1:])
