def MCD(num1, num2):
    a, b = num1, num2
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    num1 = int(input("Ingresa un número entero para num1: "))
    num2 = int(input("Ingresa un número entero para num2: "))
    print(f"El MCD de {num1} y {num2} es: {MCD(num1, num2)}")
