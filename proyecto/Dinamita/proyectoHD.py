#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
import os

nombre = "XXX"
while not os.path.isfile(nombre):
    nombre = input("Escribe el nombre del archivo (.txt): ")
    if not ".txt" in nombre:
        nombre += ".txt"

archivo = open(nombre,"r")
iterator = 0
tagsdict = {}

for line in archivo:   
    iterator += 1 
    if ":" in line:
        line.strip()
        spliter = line.split(":")
        tagsdict[str(str(spliter[0]).strip())] = iterator    

archivo.seek(0)

comandosDict = {"add" : 0,"addi" : 1,"and" : 2,"andi" : 3,"beq" : 4,"bne" : 5,"j" : 6,"jal" : 7,"jr" : 10,"lb" : 11,"or" : 12,"sb" : 13,"sll" : 14,"srl" : 15}

superString = ""
iterador = 1
for line in archivo: 
    line.strip() 
    if ":" in line:
        spliter = line.split(":")
        line = spliter[1] 
    
    spliter = line.split(",")
    superString += format(comandosDict[str(str(spliter[0]).strip())],"04b")
   
    s = comandosDict[str(str(spliter[0]).strip())]
    
    if s == 0 or s == 2 or s == 12 or s == 14 or s == 15: #tipo R
        superString += format(int(str(spliter[1]).replace("x","")),"03b") + format(int(str(spliter[2]).replace("x","")),"03b")  + format(int(str(spliter[3]).replace("x","")),"03b") + "00000" + "\n"
    elif s== 1 or s== 3 or s== 11 or s== 13 :  #tipo I
        superString += format(int(str(spliter[1]).replace("x","")),"03b") + format(int(str(spliter[2]).replace("x","")),"03b")  
        if "0x" in str(spliter[3]):
            superString += format(int(str(str(str(spliter[3]).replace("0x","")).strip()),base=16),"08b") + "\n"
        else:
            numero = int((str(spliter[3]).strip()))
            if numero < 0:
                superString += format((0xFF + numero + 1),"08b") + "\n"
            else:
                superString += format(numero,"08b") + "\n"
    elif s== 4 or s== 5:
        superString += format(int(str(spliter[1]).replace("x","")),"03b") + format(int(str(spliter[2]).replace("x","")),"03b") 
        numero = tagsdict[str(str(spliter[3]).strip())] - iterador
        if numero < 0:
            superString += format((0xFF + numero + 1),"08b") + "\n"
        else:
            superString += format(numero,"08b") + "\n"
    elif s == 6 or s == 7:
        superString += format(tagsdict[spliter[1].strip()], "014b") + "\n"
    elif s == 10 :
        superString += format(int(str(spliter[1]).replace("x","")),"03b") + "00000000000" + "\n"
    iterador += 1       

if ".txt" in nombre:
    nombre = nombre.replace(".txt","")
archivo1 = open((nombre + "-bin.txt"),"w")
archivo1.write(superString)
archivo2 = open((nombre + ".bin"),"wb")
archivo2.write(bytes(superString,"utf-8"))
archivo2.close()
archivo1.close()
archivo.close()
   
