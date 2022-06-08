#!/usr/bin/python3
def roman_to_int(roman_string):
    table = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    total, sum = 0, 0

    for i in reversed(roman_string):
        num = table[i]
        total += num if total < num*  5 else -num
    return total
        
 
