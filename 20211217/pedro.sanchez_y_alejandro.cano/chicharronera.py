from math import sqrt

A = float(input("Ingrese A: "))

B = float(input("Ingrese B: "))

C = float(input("Ingrese C: "))

def main():

    part1 = B**2-4*A*C

    if (part1) < 0:

        part1 = abs(part1)
        partReal = -B/(2*A)
        pepe = sqrt(part1)/(2*A)
        print("x1 compleja es {:.4f} + {:.4f}i".format(partReal, pepe))
        print("x2 compleja es {:.3f} - {:.3f}i".format(partReal, pepe))


    else:

        x1 = (-B+sqrt(part1))/(2*A)
        x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
        
        print("Solucion: ")

        print("X1 = ", x1)
        print("X2 = ", x2)


if __name__ == "__main__":
    main()
