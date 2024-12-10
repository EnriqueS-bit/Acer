#Parte 4: Aqui se puede ajustar la cantidad de estudiantes a almacenar
n = int(input("Ingrese la cantidad de estudiantes: "))
calificaciones = {}
for _ in range(n):
    nombre = input("Ingrese el nombre del estudiante: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))
    calificaciones[nombre] = nota

nombre_max = max(calificaciones, key=calificaciones.get)
print(f"El estudiante con la calificación más alta es {nombre_max} con una calificación de {calificaciones[nombre_max]}.")
