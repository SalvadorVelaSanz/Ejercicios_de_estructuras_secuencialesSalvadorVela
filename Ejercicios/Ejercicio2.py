# 2. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

leg1 = float(input("Ingrese el primer cateto: "))
leg2 = float(input("Ingrese el segundo cateto: "))
#Calcular la hipotenusa usando el teorema de Pitágoras
hypotenuse = (leg1**2 + leg2**2)**0.5
print("La hipotenusa es: " + str(hypotenuse))
