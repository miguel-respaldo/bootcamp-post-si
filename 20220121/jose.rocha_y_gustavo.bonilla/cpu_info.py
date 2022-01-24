#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
    CPU Info
"""

def main():
    """
        Main function
    """

    cpu_file_path = "/proc/cpuinfo"
    cpu_file = open(cpu_file_path, "r")
    cpu_info = cpu_file.read()
    cpu_file.close()

    feature_names = ("model name", "siblings", "cpu cores")
    feature_contents = list()
    cpu_info_splitted = cpu_info.split("\n")

    #for line in cpu_info_splitted: print(line)

    for feature in feature_names: 
        for line in cpu_info_splitted:
            # Do a split with ":"
            line_splitted = line.split(": ")
            feature_name = line_splitted[0]
            feature_content = line_splitted[1] # Preguntar por el segundo elemento del split que no identifica 

            # Look for keywords
            if(feature in feature_name):
                feature_contents.append(feature_content)
                #print(feature_content)
                break

    #number_of_dices = 

    print("Nombre del procesador:", feature_contents[0])
    print("No. de procesadores fisicos:", "1")
    print("No. Cores:", feature_contents[2])
    print("No. Hilos:", int(feature_contents[1])-int(feature_contents[2]))
    print("No. de procesadores lógicos:", feature_contents[1])

if __name__ == "__main__":
    main()

