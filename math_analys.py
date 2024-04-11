
class Polynome:

    def __str__(self) -> str:
        string = ""
        length = len(self.values)
        for i in range(length):
            if self.values[i] < 0:
                    
                if length - i == 1:
                    string += f" - {- self.values[i]}"
                elif length - i - 1 == 1:
                    string += f" - {- self.values[i]}x"
                else:
                    string += f" - {- self.values[i]}x^{length - i - 1}"
            elif self.values[i] > 0:

                if i == 0:
                    string += f"{self.values[i]}x^{length -i -1}"
                elif length - i == 1:
                    string += f" + {self.values[i]}"
                elif length - i - 1 == 1:
                    string += f" + {self.values[i]}x"
                else:
                    string += f" + {self.values[i]}x^{length - i - 1}"
            
        return string


    def __add__(self, poly) -> "polynome":
        length1 = len(self.values)
        length2 = len(poly.values)
        poly = poly.values

        dif = length1 - length2

        final = []
        if dif == 0:
            for i in range(length1):
                final.append(self.values[i] + poly[i])
        elif dif < 0:
            i = 0
            while dif != 0:
                final.append(poly[i])
                i += 1
                dif += 1
            for j in range(length1):
                final.append(self.values[j] + poly[j+i])
        elif dif > 0:
            i = 0
            while dif != 0:
                final.append(self.values[i])
                i += 1
                dif -= 1

            for j in range(length2):
                final.append(self.values[i+j] + poly[j])
        return Polynome(final)

    def __sub__(self, poly) -> "Polynome":
            length1 = len(self.values)
            length2 = len(poly.values)
            poly = [-x for x in poly.values]  # Negate the values of poly
            diff = length1 - length2

            final = []
            if diff == 0:
                for i in range(length1):
                    final.append(self.values[i] + poly[i])
            elif diff < 0:
                i = 0
                while diff != 0:
                    final.append(poly[i])
                    i += 1
                    diff += 1
                for j in range(length1):
                    final.append(self.values[j] + poly[j + i])
            elif diff > 0:
                i = 0
                while diff != 0:
                    final.append(self.values[i])
                    i += 1
                    diff -= 1
    
                for j in range(length2):
                    final.append(self.values[i + j] + poly[j])
            return Polynome(final)

    def dx(self) -> "Polynome":
        derivative_values = []
        for i, coeff in enumerate(self.values[::-1]):
            if i > 0:
                derivative_values.append(coeff * i)
        return Polynome(derivative_values[::-1])


    def primitive(self) -> "Polynome":
        primitive_values = [0]  # Constant term is always zero in the primitive
        for i, coeff in enumerate(self.values):
            primitive_values.append(coeff / (i + 1))
        return Polynome(primitive_values)
        

    def __init__(self, val: list[int]) -> None:
        self.values = val

        self.polynome = {}

        for i in range(len(self.values)):
            self.polynome[self.values[i]] = len(self.values) - i + 1

        
    


def factiorial(n: int) -> int:
    if n == 0:
        return 1
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


def e(n):
    e = 0
    for k in range(10):
        e += 1/factiorial(k)
    return e**n

def pi(*args) -> float:
    pi_approximation = 0
    sign = 1
    num_points = 1000000000000
    if args:
        num_points = args[0]

    for i in range(1, num_points*2, 2):
        pi_approximation += sign * (1 / i)
        sign *= -1

    pi_approximation *= 4
    return pi_approximation

    

