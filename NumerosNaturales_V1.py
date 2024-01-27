def MCD(num1, num2):
    a, b = num1, num2
    while b != 0:
        a, b = b, a % b
    return a


def mcm(num1, num2):
    mcd = MCD(num1, num2)
    minimoComunMultiplo = (num1 * num2) // mcd
    return minimoComunMultiplo
