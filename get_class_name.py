def get_class_name(myclass):
    """
    Return class name along with its non-private attributes with values.

    Parameters
    ----------
    myclass : class or object
        The class or object whose name and attributes will be returned.

    Returns
    -------
    str
        The name of the class along with its non-private attrs with values.

    Notes
    -----
    This function works by inspecting the `__dict__` attribute of the class or
    object and retrieving its non-private attributes (attributes not starting
    with '_'). The attribute names and values are then formatted into a string
    with the class name.
    """

    args = ', '.join(f'{k}={v}' for k, v in myclass.__dict__.items()
                     if not k.startswith('_'))

    return f'{myclass.__class__.__name__}({args})'
