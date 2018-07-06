# Accepted

from math import sqrt

def convex_hull(points):
    def is_counterclockwise_turn(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) >= 0

    points.sort(key=lambda point: point[0])                                
    points.sort(key=lambda point: point[1])

    right = []
    left = []

    if len(points) <= 1:
        return points
    
    for p in points:
        if len(left) > 0 and p[:-1] == left[-1][:-1] and p[-1] > left[-1][-1]:
            continue
        else:
            while len(left) >= 2 and is_counterclockwise_turn(left[-2], left[-1], p):
                left.pop()
            left.append(p)

    for p in reversed(points):
        if len(right) > 0 and p[:-1] == right[-1][:-1] and p[-1] > right[-1][-1]:
            continue
        else:
            while len(right) >= 2 and is_counterclockwise_turn(right[-2], right[-1], p):
                right.pop()
            right.append(p)

    return list(reversed(right[1:])) + list(reversed(left[1:]))

def distance(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def circumference(points):
    if len(points) < 2:
        return 0
    total = 0
    for index in range(1, len(points)):
        total += distance(points[index - 1], points[index])
    total += distance(points[0], points[-1])
    return total

def spoj_solution():
    num_tests = int(input())
    answers = []
    for i in range(num_tests):
        blank = input()
        num_sheep = int(input())
        sheep = []
        for i in range(num_sheep): 
            sheep.append(
                input().split() + [i + 1]
            )
        sheep = list(map(
            lambda s: list(map(int, s)),
            sheep
        ))
        sheep = convex_hull(sheep)
        dist = circumference(sheep)
        answers.append([sheep, dist])
    for ans in answers:
        print("%0.02f" %ans[1])
        print(' '.join(
            list(map(
                lambda s: str(s[2]),
                ans[0]
            ))
        ))
        print('')

spoj_solution()