#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    checks if the object is an inheritance of a class that inherited
    {directly or indirectly} from the specified class
    Parameters:
    obj (object) : The object to be checked.
    a_class (type) : The parent class to check against.
    Returns:
    bool : True if obj is an instance/subclass of a_class,
    False otherwise.
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
