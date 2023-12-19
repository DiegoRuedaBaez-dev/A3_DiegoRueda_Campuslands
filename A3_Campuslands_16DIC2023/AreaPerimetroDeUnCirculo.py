import math
rad = float(input("Ingrese el radio: "))

peri = 2* math.pi * rad
are = math.pi * (rad**2)

print("Perimetro: " + str(peri))
print("Area: " + str(are))