import math  # Importa el módulo math para operaciones matemáticas básicas

# Función para calcular el valor de la información
def information_value(data, attribute_index):
    total_count = len(data)  # Obtiene el número total de instancias en el conjunto de datos
    attribute_values = {}  # Inicializa un diccionario para contar los valores únicos del atributo

    # Itera sobre cada instancia en el conjunto de datos
    for item in data:
        value = item[attribute_index]  # Obtiene el valor del atributo en el índice dado
        if value not in attribute_values:
            attribute_values[value] = 0  # Inicializa el contador para un nuevo valor del atributo
        attribute_values[value] += 1  # Incrementa el contador para el valor del atributo

    info_value = 0.0  # Inicializa el valor de la información

    # Calcula el valor de la información utilizando la fórmula de entropía
    for value_count in attribute_values.values():
        probability = value_count / total_count  # Calcula la probabilidad de un valor del atributo
        info_value -= probability * math.log2(probability)  # Calcula la contribución a la entropía

    return info_value  # Devuelve el valor de la información para el atributo dado

# Función para encontrar el mejor atributo basado en el valor de la información
def find_best_attribute(data):
    num_attributes = len(data[0]) - 1  # Obtiene el número de atributos en cada instancia
    best_info_value = 0.0  # Inicializa el mejor valor de la información
    best_attribute = -1  # Inicializa el índice del mejor atributo

    # Itera sobre todos los atributos
    for i in range(num_attributes):
        info_value = information_value(data, i)  # Calcula el valor de la información para el atributo actual

        # Actualiza el mejor atributo si el valor de la información es mayor
        if info_value > best_info_value:
            best_info_value = info_value  # Actualiza el mejor valor de la información
            best_attribute = i  # Actualiza el índice del mejor atributo

    return best_attribute  # Devuelve el índice del mejor atributo

# Ejemplo de datos de entrenamiento (atributos y etiquetas)
training_data = [
    ['Soleado', 'Caliente', 'Alta', 'Débil', 'No'],
    ['Soleado', 'Caliente', 'Alta', 'Fuerte', 'No'],
    ['Nublado', 'Caliente', 'Alta', 'Débil', 'Sí'],
    ['Lluvioso', 'Templado', 'Alta', 'Débil', 'Sí'],
    ['Lluvioso', 'Frío', 'Normal', 'Débil', 'Sí'],
    ['Lluvioso', 'Frío', 'Normal', 'Fuerte', 'No'],
    ['Nublado', 'Frío', 'Normal', 'Fuerte', 'Sí'],
    ['Soleado', 'Templado', 'Alta', 'Débil', 'No'],
    ['Soleado', 'Frío', 'Normal', 'Débil', 'Sí'],
    ['Lluvioso', 'Templado', 'Normal', 'Débil', 'Sí'],
    ['Soleado', 'Templado', 'Normal', 'Fuerte', 'Sí'],
    ['Nublado', 'Templado', 'Alta', 'Fuerte', 'Sí'],
    ['Nublado', 'Caliente', 'Normal', 'Débil', 'Sí'],
    ['Lluvioso', 'Templado', 'Alta', 'Fuerte', 'No']
]

# Encontrar el mejor atributo
best_attribute_index = find_best_attribute(training_data)  # Encuentra el índice del mejor atributo
print("El mejor atributo es el número:", best_attribute_index)  # Imprime el índice del mejor atributo
