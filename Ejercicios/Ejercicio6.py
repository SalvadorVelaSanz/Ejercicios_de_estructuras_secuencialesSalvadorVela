
# 6. Escribir un programa para calcular la nota final de un examen, considerando que:
# Cada respuesta correcta suma 5 puntos.
# Cada respuesta incorrecta suma -1 puntos.
# Cada respuesta en blanco suma 0 puntos. 
# Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.
# ¿Qué tendrías que hacer para facilitar que los puntos que suman los diferentes tipos de respuestas puedan cambiar en el futuro?

correct_answers = int(input("Ingrese el número de respuestas correctas: "))
incorrect_answers = int(input("Ingrese el número de respuestas incorrectas: "))
blank_answers = int(input("Ingrese el número de respuestas en blanco: "))

points = (correct_answers * 5) + (incorrect_answers * -1) + (blank_answers * 0)
print("Puntuación total: " + str(points))

normalized_grade = points / 50
print("Nota normalizada (0-10): " + str(normalized_grade))

# Para facilitar futuros cambios en los puntos, se pueden definir variables al inicio del programa:
POINTS_CORRECT = 5
POINTS_INCORRECT = -1
POINTS_BLANK = 0
# Luego usar estas variables en el cálculo de puntos:
points = (correct_answers * POINTS_CORRECT) + (incorrect_answers * POINTS_INCORRECT) + (blank_answers * POINTS_BLANK) 
print("Puntuación total: " + str(points))
normalized_grade = points / 50
print("Nota normalizada (0-10): " + str(normalized_grade))

