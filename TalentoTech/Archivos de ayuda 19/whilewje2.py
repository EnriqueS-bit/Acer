#ejemplo de while
valor=1
suma=0
cont=0
while valor !=0:
    valor=int(input("Ingrese un valor: "))
    suma=suma+valor
    cont=cont+1
promedio=suma/(cont-1)
print("La suma es: ", suma)
print("El promedio es: ", promedio)
