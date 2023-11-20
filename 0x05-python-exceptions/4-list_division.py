#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    A function that divides elements by element 2 list

    Parameters:
    1. my_list_1: dividend list
    2. my_list_2: divisor list
    3. list_length: length of the lists

    Returns:
    New list of length list_length with all divisions
    """
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new_list.append(result)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
        finally:
            continue

    return new_list
