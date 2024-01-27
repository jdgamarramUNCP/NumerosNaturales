from NumerosNaturales import NumerosNaturales

if __name__ == '__main__':
    numeroNatural = NumerosNaturales()
    num1 = int(input("Ingresa un número entero para num1: "))
    num2 = int(input("Ingresa un número entero para num2: "))

    print(f"El MCD de {num1} y {num2} es: {numeroNatural.MCD(num1, num2)}")
    print(f"El mcm de {num1} y {num2} es: {numeroNatural.mcm(num1, num2)}")
    cociente, residuo = numeroNatural.division_entera(num1, num2)
    print(f"Cociente = {cociente} Residuo = {residuo} de dividir {num1} entre {num2}")
