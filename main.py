def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Ejemplo de uso
num1 = 36
num2 = 24
resultado = mcd(num1, num2)
print("El MCD de", num1, "y", num2, "es:", resultado)