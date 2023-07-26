#!/usr/bin/env python3
def is_prime(number):
    if number <= 1:
        return False
    
    for divsor in range(2, int(number**0.5) + 1):
        if number % divsor ==0:
            return False
        
    return True