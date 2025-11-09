# 3. Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.

total_minutes = int(input("Ingrese la cantidad de minutos: "))
hours = total_minutes // 60
minutes = total_minutes % 60
print(f"{total_minutes} minutos son {hours} horas y {minutes} minutos.")
