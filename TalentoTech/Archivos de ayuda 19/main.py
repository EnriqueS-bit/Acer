#condicionales
sueldo=int(input("Ingrese un sueldo: "))
if sueldo>=1300000:#condicional simple //
    print("Debe pagar impuesto!!")
else: # condicional compuesta
    print("No debe pagar impuesto!")
    
#condicional anidado
numero=int(input("Ingrese un numero: "))
if(numero>0):
    print("Numero positivo!")
elif numero<0:
    print("Numero negativo!")
else:
    print("Numero ingresado es cero!")