import math
a = float(input("Ingrese el cateto a: "))
b = float(input("Ingrese el cateto b: "))

c = math.sqrt((a**2) + (b**2))

print("La hipotenusa es " + str(c))