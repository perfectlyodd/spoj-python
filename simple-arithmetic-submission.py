# Accepted
# Very slow though
# TODO: Remove calls to "re" library functions

import re

def add_string_numbers(a, b):
    if a == '0':
        return b
    if b == '0':
        return a
    la = len(a)
    lb = len(b)
    ans = ''
    carry = 0
    position = 1
    while position <= max(la, lb):
        digit_a = a[-position] if position <= la else '0'
        digit_b = b[-position] if position <= lb else '0'
        new_digit = int(digit_a) + int(digit_b) + carry
        carry = int(new_digit / 10)
        new_digit = new_digit % 10
        ans = str(new_digit) + ans
        position += 1
    return ans if carry == 0 else str(carry) + ans

def subtract_string_numbers(a, b):
    la = len(a)
    lb = len(b)
    ans = ''
    borrow = 0
    position = 1
    while position <= la:
        digit_a = a[-position]
        digit_b = b[-position] if position <= lb else '0'
        new_digit = int(digit_a) - int(digit_b) - borrow
        if new_digit < 0:
            new_digit += 10
            borrow = 1
        else:
            borrow = 0
        position += 1
        ans = str(new_digit) + ans
    ans = ans.lstrip('0')
    return ans if not ans == '' else '0'

def multiply_string_number_and_string_digit(n, d, ln):
    digit = int(d)
    if digit == 0:
        return '0'
    if digit == 1:
        return n
    carry = 0
    position = 1
    ans = ''
    while position <= ln:
        digit_n = n[-position]
        new_digit = digit * int(digit_n) + carry
        carry = int(new_digit / 10)
        new_digit = new_digit % 10
        ans = str(new_digit) + ans
        position += 1
    return ans if carry == 0 else str(carry) + ans

def multiply_string_numbers(a, b):
    partial_products = []
    if a == 0 or b == 0:
        ans = 0
    else:
        la = len(a)
        ans = ''
        for digit in b:
            partial_product = multiply_string_number_and_string_digit(a, digit, la)
            partial_products.append(partial_product)
            ans = add_string_numbers(ans + '0', partial_product)
    return (partial_products, ans)

def parse_string(s):
    match = re.search(r'[-+*]', s)
    op_index = match.start()
    return (s[:op_index:], s[op_index], s[op_index + 1::])

def print_solution(a, op, b):
    la = len(a)
    lb = len(b)
    if op == '+':
        ans = add_string_numbers(a, b)
        lans = len(ans)
        num_dashes = max(lb + 1, len(ans))
        max_length = max(la, num_dashes)
        print(' ' * (max_length - la) + a)
        print(' ' * (max_length - lb - 1) + op + b)
        print(' ' * (max_length - num_dashes) + '-' * num_dashes)
        print(' ' * (max_length - lans) + ans)
        print('')
    if op == '-':
        ans = subtract_string_numbers(a, b)
        lans = len(ans)
        num_dashes = max(lb + 1, len(ans))
        max_length = max(la, num_dashes)
        print(' ' * (max_length - la) + a)
        print(' ' * (max_length - lb - 1) + op + b)
        print(' ' * (max_length - num_dashes) + '-' * num_dashes)
        print(' ' * (max_length - lans) + ans)
        print('')
    if op == '*':
        (partial_products, ans) = multiply_string_numbers(a, b)
        lans = len(ans)
        num_dashes = max(len(partial_products[-1]), lb + 1)
        max_length = max(num_dashes, lans, la)
        print(' ' * (max_length - la) + a)
        print(' ' * (max_length - lb - 1) + op + b)
        print(' ' * (max_length - num_dashes) + '-' * num_dashes)
        if len(partial_products) > 1:
            for i in range(len(partial_products)):
                partial_product = partial_products[-i-1]
                print(' ' * (max_length - len(partial_product) - i) + partial_product)
            print(' ' * (max_length - lans) + '-' * lans)
        print(' ' * (max_length - lans) + ans)
        print('')

def spoj_problem_solution():
    num_cases = int(input())
    expressions = [parse_string(input()) for i in range(num_cases)]
    for expression in expressions:
        (a, op, b) = expression
        print_solution(a, op, b)

spoj_problem_solution()