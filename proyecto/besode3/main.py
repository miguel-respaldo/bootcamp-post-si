from utilities import *

def main():
    # Nota: getType() regresa un caracter que indica el tipo de intruccion (R, I, J)

    if (getType("add") == 'R'):
        # add $2 $17 $18
        a = instructionR("add", 2, 17 , 18) # instructionR(nemonic, rd, rs, rt)

    if (getType("andi") == 'I'):
        # andi $2 $17 0x0A
        b = instructionI("andi", 2, 17, 0x0A) # instructionI(nemonic, rt, rs, imm)

    if (getType("jal") == 'J'):
        # jal 0x0x4000c
        c = instructionJ("jal", 0x400000) # instructionJ(nemonico, address)




    #print("Instruccion R: add $2 $17 $18")
    print(f"{a:32b}")

    #print("Instruccion I: andi $2 $17 $0x0A")
    print(f"{b:32b}")

    #print("Instruccion J: jal 0x4000c")
    print(f"{c:32b}")


if __name__ == "__main__":
    main()

