#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
    Code Name:  Multi-variable
    Author:     Gus_B
"""

def main():
    """
        Main function

        Boolean variables inside multi_var:
            * Carro   ->  on/off     1
            * Casa    ->  on/off     2
            * Perro   ->  on/off     4
            * Gato    ->  on/off     8
            * Pez     ->  on/off    16
            * Moto    ->  on/off    32
            * Zapato  ->  on/off    64
            * Navidad ->  on/off   128
    """

    ########## Initialization of variables ##########
    multi_var = int(0)
    variables = ["Carro", "Casa", "Perro", "Gato", "Pez", "Moto", "Zapato", "Navidad"]
    comparator = 1

    ########## Printing program information ##########
    print("\nHello, this is a multi-variable!!")
    print("Here you will be able to store 8 different boolean values in just one integer variable :)")
    print("\n\tThe 8 different boolean values are: ")
    print("\n\tVariable\tInteger Representation")

    for idx in range(8):
        print("\t", variables[idx], "   \t\t", comparator<<idx)

    ########## Requesting number for the multi-variable ##########
    multi_var = int(input("\nIntroduce the number to assign in the multi-variable: "))

    ########## Printing results ##########
    print(f'\n\tData stored in {format(multi_var,"08b")} ({multi_var}):\n')

    for idx in range(8):
        if multi_var&(comparator<<idx): print("\t", variables[idx], "   \t->\tON")
        else: print("\t", variables[idx], "   \t->\tOFF")
        
        #print(comparator)

    if multi_var&comparator: print("\nCarro:\n-I just got nine out of 10 on my driver’s test.\n-The last guy was able to get out of the way.")
    if multi_var&(comparator<<7): print('\nNavidad:\n-What goes “Oh, Oh, Oh”?\n-Santa walking backwards!')
    if (multi_var&comparator)and(multi_var&(comparator<<4))and(multi_var&(comparator<<7)): print("\nCarro, Pez, Navidad:\n-Have you seen a fish driving a car on christmas?\n-Me neither :(")
    
    print("")


if __name__ == "__main__":
    main()

