def inner_string_number(string_number, length):
    if length <= 2:
        return ''
    return string_number[1:-1:]

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

def is_bookended(string_number, length):
    return string_number[0] == string_number[length - 1]

def is_palindrome(string_number, length):
    endpoints_match = is_bookended(string_number, length)
    position = 1
    while endpoints_match and length - 2 * position >= 2:
        endpoints_match = is_bookended(string_number[position:length - position:], length - 2 * position)
        position += 1
    return length - 2 * position < 2

def bookend_numerical_string(string_number, length):
    if length == 0:
        return string_number
    done = is_bookended(string_number, length)
    while not done:
        string_number = add_one_to_string(string_number, length)
        done = is_bookended(string_number, length)
    return string_number

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

def spoj_problem_solution():
    num_cases = int(input())
    inputs = [input() for i in range(num_cases)]
    for string_number in inputs:
        print(
            next_palindrome_wrapper(string_number, False)
        )

spoj_problem_solution()