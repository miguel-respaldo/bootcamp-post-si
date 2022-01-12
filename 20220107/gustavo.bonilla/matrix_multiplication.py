#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
    Code Name: Matrix Multiplication
    Author:    Gus_B
"""

from random import randrange

def main():
    """
        Main Function
    """
    
    print("\nHi!!, this is a matrix multiplier :)\n\nIntroduce the following data:")
    
    ########################## REQUESTING DATA ##################################

    matrix_1_rows = int(input("Ammount of rows in matrix 1: "))
    matrix_1_columns = int(input("Ammount of columns in matrix 1: "))
    matrix_2_rows = int(input("Ammount of rows in matrix 2: "))
    matrix_2_columns = int(input("Ammount of columns in matrix 2: "))

    # Evaluating if the inputs can be multiplied
    if matrix_2_rows != matrix_1_columns: 
        print("\nInvalid matrix sizes :(\nThe ammount of rows in matrix 2 must be equal to the ammount of columns in matrix 1.\n")
        exit()

    print("\nDo you want matrix 1 and 2 to be filled with random numbers?")
    flag_random_text = input("[y/n] ")
    
    flag_random = True if(flag_random_text=="y" or flag_random_text=="Y") else False

    ##################### CREATING & FILLING MATRIX 1 AND 2 #####################

    matrix_1 = list()
    matrix_2 = list()

    fill_matrix(matrix_1, matrix_1_rows, matrix_1_columns, flag_random, 1)
    fill_matrix(matrix_2, matrix_2_rows, matrix_2_columns, flag_random, 2)

    ################### CREATING & FILLING RESULTANT MATRIX #####################

    matrix_result = list()

    for row_result in range(matrix_1_rows):
        matrix_result.append([])
        
        for column_result in range(matrix_2_columns):
            temp_sumatory = 0
            
            for idx in range(matrix_2_rows):
                temp_sumatory += (matrix_1[row_result][idx])*(matrix_2[idx][column_result])

            matrix_result[row_result].append(temp_sumatory)

    ##################### PRINTING RESULTS IN CONSOLE ###########################

    print("\nMATRIX 1")
    for row in range(matrix_1_rows):
        print(matrix_1[row])

    print("\nMATRIX 2")
    for row in range(matrix_2_rows):
        print(matrix_2[row])
    

    print("\nRESULTANT MATRIX")
    for row in range(matrix_1_rows):
        print(matrix_result[row])

    print("")

#################################################################################

def fill_matrix(matrix, rows, columns, flag_random, idx):
    """
        Function to Fill a Matrix with a User-Input/Random-Number
    """

    if not flag_random: print("")

    for row in range(rows):
        matrix.append([])
        
        for column in range(columns):
            if flag_random: matrix[row].append(randrange(100))
            else: matrix[row].append(int(input(f"Introduce data [{row}][{column}] of the matrix {idx}: ")))

#################################################################################

if __name__ == "__main__":
    main()
