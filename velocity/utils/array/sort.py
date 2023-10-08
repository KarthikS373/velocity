import numpy as np
import typing as tp


def argument_sort(A: tp.Array1d, I: tp.Array1d) -> None:
    """
    Sort an array and return the indices of the sorted array

    Parameters:
    A (array): The array to be sorted
    I (array): The indices of the array

    Returns:
    None

    Example:
    >>> A = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    >>> I = np.arange(len(A))
    >>> insert_argsort_nb(A, I)
    >>> print(A)
    [1 1 2 3 3 4 5 5 5 6 9]
    >>> print(I)
    [1 3 6 0 9 2 4 8 10 7 5]
    """
    for j in range(1, len(A)):
        A_j = A[j]
        I_j = I[j]
        i = j - 1
        while i >= 0 and (A[i] > A_j or np.isnan(A[i])):
            A[i + 1] = A[i]
            I[i + 1] = I[i]
            i = i - 1
        A[i + 1] = A_j
        I[i + 1] = I_j
