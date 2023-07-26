#!/usr/bin/env python3
def fibonacci_sequence(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    fibonacci_list = []
    fibonacci_list.append(0)
    fibonacci_list.append(1)

    for i in range(2, n):
        next_number = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(next_number)

    return fibonacci_list
print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))