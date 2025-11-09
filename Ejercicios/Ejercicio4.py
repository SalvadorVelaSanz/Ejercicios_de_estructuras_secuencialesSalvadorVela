# 4. Dado un número de dos cifras, diseñe un programa que permita obtener el número invertido.

number = int(input("Ingrese un número de dos cifras: "))
if 10 <= number <= 99:
    tens = number // 10
    units = number % 10
    reversed_number = units * 10 + tens
    print("El número invertido es: " + str(reversed_number))