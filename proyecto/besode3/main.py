from utilities import *

def main():
    cola = []
    n = 1
    pc = 1
    error = False
    
    nombreArchivo = input("Ingrese nombre del archivo a compilar: ")
    try:
        file = open(nombreArchivo, 'r')
    except:
        print("ESTE ARCIVO NO EXISTE")
        file = ""
        error = True
    
    for linea in file:
        tag = None
        instruccion = None
        rs, rt, rd  = None, None, None
        imm = 0
        address = 0
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

            rs, rt, rd = convertArgumentsR(nemonico, argumentos)

            codigoMaquina = instructionR(nemonico, rs, rt, rd)

        
        # Si es una instruccion tipo I se hace lo siguente
        if tipo == 'I':
            # Separar los argumentos de la instruccion y vaciarlos a una lista
            argumentos = linea.split(',')
            argumentos.pop(0)
            
            rt, rs, imm = convertArgumentsI(nemonico, argumentos)

            if nemonico != 'beq' and nemonico != 'bne':
                codigoMaquina = instructionI(nemonico, rt, rs, imm)
            

        # Si es una instruccion tipo J se hace lo siguente
        if tipo == 'J':
            # Separar los argumentos de la instruccion y vaciarlos a una lista
            argumentos = linea.split(',')

            address = argumentos[1]
            

        if tipo == 'R' or tipo == 'I' or tipo == 'J':
            # Si la entrada es correcta
            # Agreamos a una clase que guarda la informacion de cada instruccion
            cola.append(inputText(instruccion, tag, nemonico, rs, rt, rd, imm, address, pc, tipo, codigoMaquina))
            pc += 1 # Se incremente el Program Counter 
        elif linea == '':
            # Si no hay nada en una linea de texto, no hace nada
            pass
        else:
            #Si encuentra un error en alguna linea lo marca
            print(linea, f"<ERROR en la linea {n}>")
            error = True
            break
        
        n += 1 # Contador de lineas, solo se usa cuando hay un error y saber en que linea estaba



    if error == False:
        # Si no hay errores, el programa continua
        findJumps(cola) # Ingresar la lista para completar los branches y los jump
        archivoSalidaBin = open(nombreArchivo[:-4]+'.bin', 'wb')
        archivoSalidaTexto = open(nombreArchivo[:-4]+'-bin.txt', 'w')

        baits = []
        for i in cola:
            # Separar por cada 8 bits y agregarlos en a una lista
            temp = f"{i.machineCode:024b}"
            baits.append(int(temp[0:8],2))
            baits.append(int(temp[9:16],2))
            baits.append(int(temp[17:24],2))
            
            archivoSalidaTexto.write(f"{i.machineCode:018b}\n")

            #i.imprimir()
        
        # Agregar la lista con los bytes al archivo
        archivoSalidaBin.write(bytearray(baits))

        archivoSalidaBin.close()
        file.close()
    
    
    

if __name__ == "__main__":
    main()

