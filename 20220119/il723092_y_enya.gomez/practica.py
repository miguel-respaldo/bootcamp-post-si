def main(): 
    #print("Hola Mundo")
    
    f = input("Introduce el nombre del archivo (con extension) a copiar: ")
    archivo1 = open( f"copia.txt", "w")  
    archivo2 = open( f+".txt" , "r")
    archivo1.write(archivo2.read())
    print(archivi2.read())
    archivo1.close()
    archivo2.close()
	
    
