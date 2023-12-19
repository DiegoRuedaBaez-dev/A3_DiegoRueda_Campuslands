inpt = str(input("Que desea convertir Pulgadas(in) o Centimetros(cm): "))

if inpt == 'pulgadas' or inpt == 'in':

  inch = float(input("Ingrese la longitud: "))
  conver = inch * 2.54
  print(str(inch) + " = " + str(conver) + " in")

elif inpt == 'cm' or inpt == 'centimetros':

  cm = float(input("Ingrese la longitud: "))
  conver = cm / 2.54
  print(str(cm) + " = " + str(conver) + " cm")

else:
  print("Ingrese algo que tenga sentido prro hpta.")