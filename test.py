# ~~Notes on DIRVS (Direct Visibility)
# num_tests ~ 500
# 1 <= p, q <= 200
# 0 <= z <= 5000
# Ascent: At most 1 / step
# Descent: At most 3 / step
# Dijstra's algorithm?
# A*?
#   --> Cost function = height? (Higher == better)
# Data structure: 2-dimensional list?  Dictionary?
# NOTE: Columns and rows are 1-indexed


# NEEDS EXTENSIVE TESTING
def is_visible(i, j, k, l, grid):
    if grid[i - 1][j - 1] > grid[k - 1][l - 1]:        # Switch i and k in this case (so we can assume ordering later on)
        i = i + k
        k = i - k
        i = i - k
        j = j + l
        l = j - l
        j = j - l
    # Now, we can assume that (i,j) is at a lower elevation than (k,l)
    x_inc = 1 if i <= k else -1
    y_inc = 1 if j <= l else -1
    dz = grid[k - 1][l - 1] - grid[i - 1][j - 1]
    m2 = (l - j) / float(k - i)
    squares_to_check_composed = list(map(
        lambda x: [y for y in range(j, l, y_inc) if not (m2 * (x + 0.5) < y - 0.5 or m2 * (x - 0.5) > y + 0.5)],
        range(i, k, x_inc) 
    ))
    # squares_to_check_taxicab = 
    # Computing this list with a "taxicab algorithm" might be faster, but requires helpers for putting a fraction in lowest terms
    total_number_to_check = 0
    # Compute the length of the flattened array
    for x in squares_to_check_composed:
        total_number_to_check += len(x)
    z_inc = dz / float(total_number_to_check)
    result = True
    counter = 0
    for x_index in range(len(squares_to_check_composed)):
        x = i + x_index * x_inc
        for y_index in range(len(squares_to_check_composed[x_index])):
            y = squares_to_check_composed[x_index][y_index]
            result = result and grid[x - 1][y - 1] <= grid[i - 1][j - 1] + counter * z_inc
    return result

# To implement A*, we need a good heuristic:
#   - Just use the straight-line distance
# Also need a priority queue       

#~~Notes on I-Keyboard (IKEYB)
#   - Alphabetical order required
#   - Any number of letters can be assigned to a key
#   - Input:
#       - T <= 2000
#       - num_keys num_letters
#       - char[] key_names
#       - char[] letter_names
#       - <F_i> <= 100000
#   - Output:
#       - Optimal keyboard for each case
#       - "Price" for each key = frequency * position
#       - Multiple possible solutions:
#           - Maximize number of letters assigned to last keys
#       - Format:
#           - Keypad #n:
#           - <key char>: <non-separated letter list>
#           - <blank line>

# Problems:
#   - Exhaustive search required?
#       - Local extrema sufficient?
#   - Can model decision tree as graph
#       --> A* search
#       - Cost must be additive (associated to edges, not nodes)

# Greedy approach:
#   - Begin with partitions placed before highest frequencies






