#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""
Proyecto Final
Equipo:
    Antonio Josué Rodríguez Barera
    Javier de Alba Pérez
"""
#Estas liberias se importan de los programas mnemonic y registros creados en el mismo directorio
import mnemonic    
import registros
#########################
import os
import argparse

#etiquetas_archivo=[]
#num_etiquetas=[]
PC=1
etiquetas={}

#Aqui se define la funcion para poder dar el numero de registro para cada función
def linea_instruccion(opcode,rs,rt,rd):
    linea= ""
        
    if(opcode==0): #add
        linea += "{:04b}".format(opcode)
        linea += "{:03b}".format(rs)
        linea += "{:03b}".format(rt)
        linea += "{:03b}".format(rd)
        linea += "00000"
    elif(opcode==1):#addi
        linea += "{:04b}".format(opcode)
        linea += "{:03b}".format(rs)
        linea += "{:03b}".format(rt)
        if int(rd) < 0:
            rd=(int(rd)^0xff + 1) & 0xff
            linea+="{:08b}".format(rd)
        else:
            linea+="{:08b}".format(rd)
    elif(opcode==2):#and
        linea += "{:04b}".format(opcode)
        linea += "{:03b}".format(rs)
        linea += "{:03b}".format(rt)
        linea += "{:03b}".format(rd)
        linea += "00000"        
    elif(opcode==3): #andi
        linea += "{:04b}".format(opcode)
        linea += "{:03b}".format(rs)
        linea += "{:03b}".format(rt)
        if int(rd)<0:
            rd=(int(rd)^0xff + 1) & 0xff
            linea+="{:08b}".format(rd)
        else:
            linea+="{:08b}".format(rd)
    elif(opcode==4): #beq
        linea += "{:04b}".format(opcode)
        linea += "{:03b}".format(rs)
        linea += "{:03b}".format(rt)
        if int(rd) < PC:
            rd=-int(rd)
            rd=(rd^0xff + 1) & 0xff
            linea+="{:08b}".format(rd)
        else:
            rd-=rd
            linea+="{:08b}".format(rd)        
    elif(opcode==5): #bne
        linea += "{:04b}".format(opcode)
        linea += "{:03b}".format(rs)
        linea += "{:03b}".format(rt)
        if int(rd) < PC:
            rd=-int(rd)
            rd=(rd^0xff + 1) & 0xff
            linea+="{:08b}".format(rd)
        else:
            rd-=int(rd)
            linea+="{:08b}".format(int(rd))

    elif(opcode==6): #j
        linea += "{:04b}".format(opcode)
        linea += "{:014b}".format(rs)

    elif(opcode==7): #jal
        linea += "{:04b}".format(opcode)
        linea += "{:014b}".format(rs)

    elif(opcode==10): #jr
        linea += "{:04b}".format(opcode)
        linea += "{:03b}".format(rs)
        linea += "00000000000"

    elif(opcode==11): #lb
        linea += "{:04b}".format(opcode)
        linea += "{:03b}".format(rs)
        linea += "{:03b}".format(rd)
        if int(rt)<0:
            rt=(rt^0xff+1) &0xff
            linea += "{:08}".format(int(rt))
        else:
            linea += "{:08}".format(int(rt))

    elif(opcode==12): #or
        linea += "{:04b}".format(opcode)
        linea += "{:03b}".format(rs)
        linea += "{:03b}".format(rt)
        linea += "{:03b}".format(rd)
        linea += "00000"

    elif(opcode==13): #sb
        linea += "{:04b}".format(opcode)
        linea += "{:03b}".format(rs)
        linea += "{:03b}".format(rd)
        if int(rt)<0:
            rt=(rt^0xff+1) &0xff
            linea += "{:08}".format(int(rt))
        else:
            linea += "{:08}".format(int(rt))

    elif(opcode==14): #sll
        linea += "{:04b}".format(opcode)
        linea += "{:03b}".format(rs)
        linea += "{:03b}".format(rt)
        linea += "{:03b}".format(rd)
        linea += "00000"

    elif(opcode==15): #srl
        linea += "{:04b}".format(opcode)
        linea += "{:03b}".format(rs)
        linea += "{:03b}".format(rt)
        linea += "{:03b}".format(rd)
        linea += "00000"
    return linea

#Función de escriturade archivos
def write_file(lineas_bin, filename, es_texto):
    archivo = open(filename, 'w')
    if es_texto:
        for linea in lineas_bin:
            archivo.write(linea)
            archivo.write('\n')
    else:
        pass
    archivo.close()


#Aqui vamos a encontrar el valor de las etiquetas
def obtener_etiquetas(etiqueta):
    linea=-1
    for i in range(len(etiquetas)):
        if etiquetas[i].lower()==etiqueta.strip().lower():
            linea=num_etiquetas[i]
            break
    return linea


####Se abre el archivo###

#####PRIMERO SE LEE LA ENTRADA DEL ARCHIVO####

def main():
    """
    Función principal del programa
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("archivo", help="Archivo de entrada")
    parser.add_argument("-t", "--text",
                        action="store_true", dest="gen_texto", default=False,
                        help="Generar código en texto")
    parser.add_argument("-o", "--output",
                        action="store", dest="nombre_de_salida", default="salida.o",
                        help="Nombre de archivo de salida")

    args = parser.parse_args()
    lineas_bin=[]
    
    if not os.path.exists(args.archivo):
        print(f"No se encuentra el archivo {args.archivo}")
        exit(1)
    
    else:
        global PC
        global etiquetas
        global num_etiquetas
        opcode=0
        rd=0
        rt=0
        rs=0
        #abrimos el archivo a leer    
        archivo = open(args.archivo)
        '''
        separacion=args.nombre_de_salida.split(".")
        extension=separacion[len(separacion)-1] 
        print(extension)
        if extension == "txt":
            modo="wt"
        else:
            modo = "wb"

        archivo_salida=open(args.nombre_de_salida, modo)
        '''
        for linea1 in archivo:
            #se buscan las etiquetas que existan en el texto
            if ":" in linea1:
                etiquetas[linea1.split(":")[0].strip()]=PC
                #etiquetas_archivo.append(linea1.split(":")[0].strip())
                #num_etiquetas.append(PC)
            PC+=1
        
        #se regresa al principio del archivo 
        archivo.seek(0)
        PC=1

        for linea1 in archivo:
            linea1=linea1.strip()
            #busca etiquetas
            if ":" in linea1:
                linea1=linea1.split(":")[1].strip()

            #separamos los argumentos con una coma aqui ya no hay etiquetas ni espacios
            lista_sin_etiquetas = linea1.split(",")
            for x in range(len(lista_sin_etiquetas)):
                val = lista_sin_etiquetas[x].strip()
                if '0x' in val:
                    val = int(val[2:], 16)
                if val in etiquetas:
                    lista_sin_etiquetas[x]=etiquetas[val]
                else:
                    lista_sin_etiquetas[x]=val
            print (lista_sin_etiquetas)
            #ejecutamos la funcion mnemonicos para obtener todos los opcode y tipo de función de cada instruccion en el archivo            
            for x in range(len(lista_sin_etiquetas)):
                if x==0:
                    opcode=mnemonic.mnemonicos(lista_sin_etiquetas[0])
                    print(opcode)
                elif x==1:
                    rd=int(registros.registros(lista_sin_etiquetas[1]))
                    if rd==-1:
                       rd=int(lista_sin_etiquetas[1])
                    print(rd)
                elif x==2:
                    rs=int(registros.registros(lista_sin_etiquetas[2]))
                    if rs==-1:
                       rs=int(lista_sin_etiquetas[2])
                    print(rs)
                elif x==3:
                    rt=int(registros.registros(lista_sin_etiquetas[3]))  
                    if rt==-1:
                       rt=int(lista_sin_etiquetas[3])
                    print(rt)
            
            binario=linea_instruccion(opcode,rd,rs,rt)
            lineas_bin.append(binario)
            '''
            archivo_salida.write(binario)
            archivo_salida.write("\n")
            '''
            print(binario)
        '''
        archivo_salida.close()
        '''
        archivo.close()

    print("Archivo:",args.archivo)
    print("Salida:",args.nombre_de_salida)
    print("en texto:",args.gen_texto)
    print(etiquetas)
    print(lineas_bin)
    write_file(lineas_bin, args.nombre_de_salida, args.gen_texto)



if __name__ == "__main__":
    main()
