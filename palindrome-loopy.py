# Problem: Find the next palindrome
# UPDATE: Submitted to SPOJ, time limit exceeded

import time

# Loopy
def inner_string_number(string_number, length):
    if length <= 2:
        return ''
    return string_number[1:-1:]

# Loopy implementation passes simple-palindrome-test.txt
# Doesn't pass palindrome-test.txt
# Update: Passes all tests
def add_one_to_string(string_number, length):
    if length == 0:
        return '1'
    position = 1
    carry = True
    while carry:
        char = string_number[length - position]
        if position > length:
            string_number = '1' + string_number
            carry = False
        elif '0' <= char and char <= '8':
            carry = False
            string_number = string_number[:length - position:] + chr(ord(char) + 1) + string_number[length - position + 1::]
        else:
            string_number = string_number[:length - position:] + '0' + string_number[length - position + 1::]
            position += 1
    return string_number

# Loopy
def is_bookended(string_number, length):
    return string_number[0] == string_number[length - 1]

# Loopy implementation passes all tests
def is_palindrome(string_number, length):
    endpoints_match = is_bookended(string_number, length)
    position = 1
    while endpoints_match and length - 2 * position >= 2:
        endpoints_match = is_bookended(string_number[position:length - position:], length - 2 * position)
        position += 1
    return length - 2 * position < 2

# Loopy implementation passes all tests
def bookend_numerical_string(string_number, length):
    if length == 0:
        return string_number
    done = is_bookended(string_number, length)
    while not done:
        string_number = add_one_to_string(string_number, length)
        done = is_bookended(string_number, length)
    return string_number

# Loopy implementation passes all tests
def next_palindrome(string_number, length):
    position = 0
    done = length - 2 * position < 2
    while not done:
        string_number = \
            string_number[:position:] \
            + bookend_numerical_string(string_number[position:length-position:], length - 2 * position) \
            + string_number[length-position::]
        position += 1
        done = length - 2 * position < 2
    return string_number
    
# Acceptably recursive (depth <= 2)
def next_palindrome_wrapper(string_number, palindrome_status_known):
    length = len(string_number)
    if length == 0:
        return '1'
    if not palindrome_status_known:
        if is_palindrome(string_number, length):
            return next_palindrome_wrapper(
                add_one_to_string(string_number, length),
                True
            )
    return next_palindrome(string_number, length)

# Loopy
def spoj_problem_solution():
    num_cases = int(input())
    inputs = [input() for i in range(num_cases)]
    for string_number in inputs:
        print(
            next_palindrome_wrapper(string_number, False)
        )

# Loopy
def test_solution_with_file():
    print('Enter a filename:')
    filename = input()
    stream = open(filename, 'r')
    inputs = stream.readlines()
    stream.close()
    # for string_number in inputs:
    #     print(string_number.split())
    counter = 1
    start = time.time()
    for string_number in inputs:
        processed_string_array = string_number.split()
        if not len(processed_string_array) == 0:
            processed_string_number = string_number.split()[0]
        else:
            processed_string_number = ''
        if len(processed_string_number) == 0 or not processed_string_number[0] == '#':
            print(
                str(counter) + ': ' + processed_string_number + ' --> ' + next_palindrome_wrapper(processed_string_number, False)
            )
        counter += 1
    print('----- Execution time = %s s -----' %(time.time() - start))

#spoj_problem_solution()
test_solution_with_file()