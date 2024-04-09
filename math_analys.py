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


    def __init__(self, val: list[int]) -> None:
        self.values = val

        self.polynome = {}

        for i in range(len(self.values)):
            self.polynome[self.values[i]] = len(self.values) - i + 1

        
    

p = Polynome([2, -3, 0, 4])  # Example polynomial 2x^3 - 3x^2 + 4
derivative_p = p.dx()  # Compute the derivative
print(derivative_p)  # Output: "6x^2 - 6x"
