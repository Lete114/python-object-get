from typing import Any, Union, Dict, List


def get(obj: Union[Dict, List], path: str, default: Any = None) -> Any:
    """
    Get the value at the given property path of the object, or return the default value if not found.

    Parameters:
    obj (dict or list): The object to get the value from.
    prop (str): The property path to get the value for.
    default: The default value to return if the property path is not found.

    Returns:
    The value at the given property path of the object, or the default value if not found.
    """
    try:
        path = path.replace("[", ".").replace("]", "")
        arr = path.split(".")
        tmp = obj
        for i in arr:
            if isinstance(tmp, dict):
                tmp = tmp.get(i, default)
            elif isinstance(tmp, list):
                i = int(i)
                tmp = tmp[i]
            else:
                return default
        return tmp
    except (ValueError, IndexError):
        return default
