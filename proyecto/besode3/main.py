from utilities import *

def main():
    file = open("codigo3.txt", 'r')
    
    cola = []
    
    pc = 0x400000
    
    

    for linea in file:
        tag = None
        instruccion = None
        rs, rt, rd  = None, None, None
        imm = 0
        addres = 0
        codigoMaquina = 0

        # Limpia el texto de caracteres no deseados
        linea = linea.strip()
        linea = linea.replace('\t', '')
        linea = linea.replace(' ', '')

        # Las etiquetas siempre llevan un ':'
        indexTag = linea.find(':')
        if indexTag > 0:
            # Si tiene una etiqueta, lo que va antes de ':' se guarda como la etiqueta, el resto es la instruccion
            tag = linea[ : indexTag]
            instruccion = linea[indexTag+1 : ]
        else:
            # Cuando no tiene etiqueta, la linea entera es la instruccion
            tag = None
            instruccion = linea
        
        # El nemonico al estar separado por ',' el texto antes de la primer coma es el nemonico
        nemonico = instruccion[ : instruccion.find(',')]

        # Se averigua que tipo de instruccion es
        tipo = getType(nemonico)




        # Si es una instruccion tipo R se hace lo siguente
        if tipo == 'R':
            # Separar los argumentos de la instruccion y vaciarlos a una lista
            argumentos = linea.split(",")
            argumentos.pop(0)

            # Las instrucciones "jr" solo usan rs; el resto ocupan rs, rt, rd
            if nemonico == "jr":
                rs = int(argumentos[0][1: ])
                rt, rd = 0, 0
            else:
                rd = int(argumentos[0][1: ])
                rs = int(argumentos[1][1: ])
                rt = int(argumentos[2][1: ])

            codigoMaquina = instructionR(nemonico, rs, rt, rd)

            #print(f"{codigoMaquina:032b}")




        # Si es una instruccion tipo I se hace lo siguente
        if tipo == 'I':
            # Separar los argumentos de la instruccion y vaciarlos a una lista
            argumentos = linea.split(',')
            argumentos.pop(0)
            
            # Convertir en numeros los argumentos
            for i in range(len(argumentos)):
                if argumentos[i].isnumeric(): # Para numeros positivos
                    argumentos[i] = int(argumentos[i]) 
                elif argumentos[i].startswith('-') and argumentos[i][1:].isnumeric(): # Para numeros negativos
                    argumentos[i] = int(argumentos[i][1:]) 
                    argumentos[i] *= -1
                    argumentos[i] = argumentos[i] + (1 << 16)
                elif argumentos[i].startswith('x'): # Para numeros los registros
                    argumentos[i] = int(argumentos[i][1 :])
                elif argumentos[i].startswith('0x'): # Para numeros hexadecimales
                    argumentos[i] = int(argumentos[i], 16)
                elif argumentos[i].startswith('0b'): # Para numeros binarios
                    argumentos[i] = int(argumentos[i], 2)
            
            rt = argumentos[0]
            rs = argumentos[1]
            imm = argumentos[2]

            if nemonico == 'beq' or nemonico == 'bne':
                pass
            else:
                rt = argumentos[0]
                rs = argumentos[1]
                imm = argumentos[2]
                
                codigoMaquina = instructionI(nemonico, rt, rs, imm)
                #print(f"{codigoMaquina:032b}")


        # Si es una instruccion tipo J se hace lo siguente
        if tipo == 'J':
            # Separar los argumentos de la instruccion y vaciarlos a una lista
            argumentos = linea.split(',')

            addres = argumentos[1]
            
            






        # Agreamos a una clase que guarda la informacion de cada instruccion
        cola.append(input(instruccion, tag, nemonico, rs, rt, rd, imm, addres, pc, tipo, codigoMaquina))
        
        pc += 4 # Se incremente el Program Counter 4 bytes


    
    for i in cola:
        if i.addres != None:
            for j in cola:
                if i.addres == j.tag: # Aquí solo entran las instrucciones de tipo J
                    i.addres = j.pc
                    i.addres = i.addres >> 2
                    
                    i.machineCode = instructionJ(i.nemonic, addres)
                    

                
                if i.imm == j.tag: # Aqui entran los bne y beq
                    #print(i.imm, j.tag)
                    i.imm = (j.pc >> 2) - (i.pc >> 2)
                    
                    i.machineCode = instructionI(i.nemonic, i.rt, i.rs, i.imm)
                    

        i.imprimir()
    
    

if __name__ == "__main__":
    main()

