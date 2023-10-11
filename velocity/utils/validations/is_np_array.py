import numpy as np


import numpy as np
import typing as tp


def is_np_array(arg: tp.Any) -> bool:
    """
    Check whether the argument is a numpy array.

    Args:
        arg: Any argument to be checked.

    Returns:
        bool: True if the argument is a numpy array, False otherwise.
    """
    return isinstance(arg, np.ndarray)
