#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
    CPU Info
"""

import os.path

def main():
    """
        Main function
    """

    cpu_file_path = input("Introduce el nombre del archivo a analizar: ")
    
    if cpu_file_path=="" or (not os.path.isfile(cpu_file_path)):
        cpu_file_path = "/proc/cpuinfo"
    
    cpu_file = open(cpu_file_path, "r")
    cpu_info = cpu_file.read()
    cpu_file.close()

    feature_names = ("physical id", "model name", "siblings", "cpu cores")
    dice_contents = list()
    physical_ids = list()
    physical_cores = 0
    processors_splitted = cpu_info.split("\n\n")

    for processor_info in processors_splitted:
        cpu_info_splitted = processor_info.split("\n")
        feature_contents = list()
        actual_physical_core = 0

        for feature in feature_names: 
            for line in cpu_info_splitted:
                # Do a split with ": "
                if ": " in line:
                    line_splitted = line.split(": ")
                    feature_name = line_splitted[0]
                    feature_content = line_splitted[1] 

                    # Look for keywords
                    if feature in feature_name:
                        #print(feature_content)
                        if feature == feature_names[0]:
                            #physical_cores = int(feature_content)
                            actual_physical_core = int(feature_content)
                            
                            if not (feature_content in physical_ids):
                                physical_ids.append(feature_content)
                            else: 
                                break
                                break

                        else:
                            feature_contents.append(feature_content)
                            if (feature == feature_names[3]) and (actual_physical_core+1)>physical_cores:
                                physical_cores += 1
                                dice_contents.append(feature_contents)

                            break

    idx = 0
    cores_total = 0
    threads_total = 0
    logic_total = 0

    for dice in dice_contents:
        print("\nInformación del dice:", idx, "\n")
        idx += 1
        print("Nombre del procesador:", dice[0])
        print("No. de procesadores fisicos:", physical_cores)
        print("No. Cores:", dice[2])
        cores_total += int(dice[2])
        print("No. Hilos:", int(dice[1])-int(dice[2]))
        threads_total += int(dice[1])-int(dice[2])
        print("No. de procesadores lógicos:", dice[1])
        logic_total += int(dice[1])
        # print(feature_contents)
        print("")

    print("\n///////////////////////////////////\n\nInformación general:", idx, "\n")
    print("No. de procesadores fisicos:", physical_cores)
    print("No. total de Cores:", cores_total)
    print("No. total de Hilos:", threads_total)
    print("No. total de procesadores lógicos:", logic_total)
    print("")


if __name__ == "__main__":
    main()

