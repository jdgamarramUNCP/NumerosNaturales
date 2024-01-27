from MCD_V2 import MCD


def mcm(num1, num2):
    mcd = MCD(num1, num2)
    minimoComunMultiplo = (num1 * num2) // mcd
    return minimoComunMultiplo


if __name__ == '__main__':
    num1 = int(input("Ingresa un número entero para num1: "))
    num2 = int(input("Ingresa un número entero para num2: "))
    print(f"El MCD de {num1} y {num2} es: {mcm(num1, num2)}")
