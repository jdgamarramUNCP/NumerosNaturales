from NumerosNaturales_V1 import *

if __name__ == '__main__':
    num1 = int(input("Ingresa un número entero para num1: "))
    num2 = int(input("Ingresa un número entero para num2: "))

    print(f"El MCD de {num1} y {num2} es: {MCD(num1, num2)}")
    print(f"El mcm de {num1} y {num2} es: {mcm(num1, num2)}")
