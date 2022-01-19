#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

file_name = input("Escribe el nombre del archivo a copiar: " )

with open(file_name) as f:
    #----
    file_content = f.read() # tenemos todo el contenido del archivo en la variable
    
    #--se cierra automagicamente

with open("copia.txt","w") as f:
    f.write(file_content) # excribimos el contenido en el nuevo archivo
    
print("copiado con etsito")
print("")
with open("copia.txt") as f:
    for x in f:
        print(x.strip())
        
 
