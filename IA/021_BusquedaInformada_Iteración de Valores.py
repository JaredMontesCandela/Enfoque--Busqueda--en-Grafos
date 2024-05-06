# Definir un diccionario de estudiantes y sus calificaciones
students = {
    'Juan': [85, 90, 88],
    'María': [92, 89, 94],
    'Carlos': [78, 85, 80]
}

# Inicializar un diccionario para almacenar los promedios de calificaciones de cada estudiante
average_grades = {}

# Iterar sobre cada estudiante y sus calificaciones
for student, grades in students.items():
    # Calcular el promedio de calificaciones
    average_grade = sum(grades) / len(grades)
    # Almacenar el promedio de calificaciones en el diccionario de promedios
    average_grades[student] = average_grade

# Encontrar al estudiante con el promedio de calificaciones más alto
best_student = max(average_grades, key=average_grades.get)

# Imprimir los promedios de calificaciones de cada estudiante
print("Promedio de calificaciones de cada estudiante:")
for student, average_grade in average_grades.items():
    print(f"{student}: {average_grade:.2f}")

# Imprimir el estudiante con el promedio más alto
print(f"\nEl estudiante con el promedio más alto es: {best_student} con un promedio de {average_grades[best_student]:.2f}")
