def numberize_list(l):
    return list(map(
        lambda elem: int(elem) if elem.isnumeric() else 0,
        l
    ))

def stringify_list(l):
    return list(map(
        lambda elem: str(elem),
        l
    ))

def differences(l):
    if len(l) <= 1:
        return ([], True)
    is_constant = True
    result = []
    for index in range(len(l) - 1):
        result.append(l[index + 1] - l[index])
        is_constant = is_constant and result[-1] == result[-2] if len(result) > 1 else True
    return (result, is_constant)

# Passes basic console test
def reduce_sequence(l):
    if len(l) <= 1:
        return [l]
    result = [l]
    is_constant = True
    for index in range(len(l) - 1):
        is_constant = is_constant and l[index] == l[index + 1]
    while not is_constant:
        (diff, const) = differences(l)
        l = diff
        if len(l) > 0:
            result.append(l)
        is_constant = const
    return result

def test_reduce_sequence():
    while True:
        print("Enter input sequence:")
        l = input().split()
        print(l)
        l = numberize_list(l)
        print(reduce_sequence(l))

# Passes basic console test
def continue_sequence(s):
    length = len(s)
    if length <= 1:
        s[0].append(s[0][-1])
    else:
        for index in range(2, length + 1):
            s[length - index].append(s[length - index + 1][-1] + s[length - index][-1])
    return s

def test_continue_sequence():
    while True:
        print("Enter input sequence:")
        l = input().split()
        l = numberize_list(l)
        l = reduce_sequence(l)
        print(continue_sequence(l))

# Passes SPOJ sample input test
def spoj_solution():
    num_test_cases = int(input())
    target_lengths = []
    sequences = []
    for i in range(num_test_cases):
        lengths = numberize_list(input().split())
        target_lengths.append((sum(lengths), lengths[1]))
        sequences.append(numberize_list(input().split()))
    sequences = list(map(
        reduce_sequence,
        sequences
    ))
    for index in range(num_test_cases):
        while len(sequences[index][0]) < target_lengths[index][0]:
            sequences[index] = continue_sequence(sequences[index])
        print(
            ' '.join(
                stringify_list(sequences[index][0][-target_lengths[index][1]::])
            )
        )

#test_reduce_sequence()
#test_continue_sequence()
spoj_solution()