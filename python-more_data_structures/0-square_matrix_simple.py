#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []  #e
    
    for row in matrix:  
        squared_row = list(map(lambda x: x ** 2, row))  #q
        new_matrix.append(squared_row)  
    #gj
    
    return new_matrix  

