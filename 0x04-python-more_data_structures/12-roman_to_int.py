#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or roman_string is None:
        return 0
    if type(roman_string) != str:
        return 0
    value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    length = len(roman_string)
    while i < length:
        if i+1 < length and value[roman_string[i]] < value[roman_string[i+1]]:
            total += (value[roman_string[i+1]] - value[roman_string[i]])
            i += 2
        else:
            total += value[roman_string[i]]
            i += 1

    return total
