class NumerosNaturales():
    def MCD(self, num1, num2):
        a, b = num1, num2
        while b != 0:
            a, b = b, a % b
        return a


    def division_entera(self, dividendo, divisor):
        cociente = 0
        while dividendo >= divisor:
            dividendo -= divisor
            cociente += 1
        return cociente, dividendo

    def mcm(self, num1, num2):
        mcd = self.MCD(num1, num2)
        minimoComunMultiplo = (num1 * num2) // mcd
        return minimoComunMultiplo
