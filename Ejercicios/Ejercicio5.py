# 5. Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
# Escribir un programa que determine la hora de llegada a la ciudad B.

h = int(input("Ingrese la hora de salida (HH): "))
m = int(input("Ingrese los minutos de salida (MM): "))
s = int(input("Ingrese los segundos de salida (SS): "))
travel_seconds = int(input("Ingrese el tiempo de viaje en segundos (T): "))
total_seconds = h * 3600 + m * 60 + s + travel_seconds
arrival_hour = (total_seconds // 3600) % 24 #% 24 para formato 24 horas
arrival_minute = (total_seconds % 3600) // 60 #% 60 para formato 60 minutos
arrival_second = total_seconds % 60 #% 60 para formato 60 segundos
print(f"La hora de llegada es: {arrival_hour:02}:{arrival_minute:02}:{arrival_second:02}")