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

    cpu_info_splitted = cpu_info.split("\n")


if __name__ == "__main__":
    main()

