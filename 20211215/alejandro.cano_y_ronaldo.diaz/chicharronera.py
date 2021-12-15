from math import sqrt

A = int(input("Ingrese A: "))

B = int(input("Ingrese B: "))

C = int(input("Ingrese C: "))


def main():

    if ((B**2)-4*A*C) < 0:
        
        print("Solucion compleja")

    else:

        x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
        x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
        
        print("Solucion: ")

        print("X1 = ", x1)
        print("X2 = ", x2)


if __name__ == "__main__":
    main()
