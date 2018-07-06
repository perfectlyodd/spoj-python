# Problem: Find the next palindrome
# Status: Runtime error on submit
# TODO: Check add_one_to_string error handling and edge cases
# UPDATE: Algorithm appears to work on all relevant edge cases.  Recursion depth exceeded on extremely large inputs.

def inner_string_number(string_number, length):
    if length <= 2:
        return ''
    return string_number[1:-1:]

def add_one_to_string(string_number, length):
    if length == 0:
        return '1'
    last_char = string_number[length - 1]
    if '0' <= last_char and last_char <= '8':
        return string_number[:-1] + chr(ord(last_char) + 1)
    elif last_char == '9':
        return add_one_to_string(string_number[:-1], length - 1) + '0'
    else:
        return '0000'

def is_bookended(string_number, length):
    return string_number[0] == string_number[length - 1]

def is_palindrome(string_number, length):
    if length < 2:
        return True
    return is_bookended(string_number, length) and is_palindrome(inner_string_number(string_number, length), length - 2)

def bookend_numerical_string(string_number, length):
    if length == 0:
        return string_number
    if is_bookended(string_number, length):
        return string_number
    else:
        return bookend_numerical_string(
            add_one_to_string(string_number, length),
            length
        )
        ## Note: Passing 'length' as a parameter is intended to save overhead by avoiding repeated
        ## calls to 'len()'.  In this return statement, it is safe to assume that the length of the
        ## string returned by 'add_one_to_string(...)' will have the same length as the original, because
        ## the only case where this is not true should trigger the first 'return' statement.
        
def next_palindrome(string_number, length):
    if length < 2:
        return string_number
    ans = bookend_numerical_string(string_number, length)
    return ans[0] + next_palindrome(inner_string_number(ans, length), length - 2) + ans[0]

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

def test_solution_with_file():
    print('Enter a filename:')
    filename = input()
    stream = open(filename, 'r')
    inputs = stream.readlines()
    stream.close()
    # for string_number in inputs:
    #     print(string_number.split())
    counter = 1
    for string_number in inputs:
        processed_string_array = string_number.split()
        if not len(processed_string_array) == 0:
            processed_string_number = string_number.split()[0]
        else:
            processed_string_number = ''
        if len(processed_string_number) == 0 or not processed_string_number[0] == '#':
            print(
                str(counter) + ': ' + next_palindrome_wrapper(processed_string_number, False)
            )
        counter += 1

#spoj_problem_solution()
test_solution_with_file()