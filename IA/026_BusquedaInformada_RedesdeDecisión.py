import math
# Definir una función para calcular la entropía de un conjunto de datos
def entropy(data):
    total_count = len(data)
    class_counts = {}  # Contador para cada clase
    for item in data:
        # Contar las ocurrencias de cada clase
        label = item[-1]  # Último elemento es la etiqueta/clase
        if label not in class_counts:
            class_counts[label] = 0
        class_counts[label] += 1

    entropy_val = 0.0
    # Calcular la entropía usando la fórmula de la entropía
    for count in class_counts.values():
        probability = count / total_count
        entropy_val -= probability * math.log2(probability)
    return entropy_val

# Definir una función para dividir los datos en subconjuntos basados en un atributo dado
def split_data(data, attribute_index, attribute_value):
    sub_data = []
    for item in data:
        if item[attribute_index] == attribute_value:
            sub_data.append(item)
    return sub_data

# Definir una función para encontrar el mejor atributo para dividir
def find_best_split(data):
    num_attributes = len(data[0]) - 1  # Excluimos la columna de etiquetas
    base_entropy = entropy(data)
    best_info_gain = 0.0
    best_attribute = -1

    # Iterar sobre todos los atributos
    for i in range(num_attributes):
        attribute_values = set([item[i] for item in data])  # Obtener los valores únicos del atributo
        new_entropy = 0.0
        # Calcular la entropía para cada valor del atributo y sumarlas ponderadas
        for value in attribute_values:
            sub_data = split_data(data, i, value)
            probability = len(sub_data) / len(data)
            new_entropy += probability * entropy(sub_data)
        # Calcular la ganancia de información
        info_gain = base_entropy - new_entropy
        # Actualizar el mejor atributo si la ganancia de información es mayor
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_attribute = i

    return best_attribute

# Definir una función para construir el árbol de decisión recursivamente
def build_decision_tree(data):
    # Si todos los elementos tienen la misma etiqueta, devolver esa etiqueta
    if len(set(item[-1] for item in data)) == 1:
        return data[0][-1]
    # Si no hay más atributos para dividir, devolver la etiqueta más común
    if len(data[0]) == 1:
        return max(set(item[-1] for item in data), key=[item[-1] for item in data].count)
    
    # Encontrar el mejor atributo para dividir
    best_attribute = find_best_split(data)
    decision_tree = {best_attribute: {}}
    # Dividir los datos en subconjuntos basados en el mejor atributo
    attribute_values = set([item[best_attribute] for item in data])
    for value in attribute_values:
        sub_data = split_data(data, best_attribute, value)
        # Construir el árbol de decisión para cada subconjunto
        decision_tree[best_attribute][value] = build_decision_tree(sub_data)
    return decision_tree

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

# Construir el árbol de decisión
decision_tree = build_decision_tree(training_data)
print(decision_tree)
