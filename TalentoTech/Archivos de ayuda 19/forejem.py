#ejemplo de for 
cantidad=0
menor=0
n=int(input("Cuantos valores quiere ingresar?"))
for f in range(n):
    valor=int(input("Ingrese un valor: "))
    if valor>=1000:
        cantidad=cantidad+1 
    else:
        menor=menor+1
print("La cantidad de numeros ingresados mayores o iguales a 1000 son: ",cantidad)
print("La cantidad de numeros ingresados menores a 1000 son: ",menor)
    
