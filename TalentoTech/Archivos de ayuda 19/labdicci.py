# crear el diccionario
calificaciones={
    "Pablo":3.0,
    "Maria":4.5,
    "Ana":4.2,
    "Juan":4.3
}

nombre_max = max(calificaciones, key=calificaciones.get)
print(f"El estudiante con la calificación más alta es {nombre_max} con una calificación de {calificaciones[nombre_max]}.")
