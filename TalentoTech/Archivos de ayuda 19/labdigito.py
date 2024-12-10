# cantidad de digitos
numero=int(input("Ingrese un nuemro: de 0 a 999"))
if numero < 10:
    print("El numero ",numero," tiene un digito!")
elif numero >=10 and numero <100:
    print("El numero ",numero," tiene dos digitos!")
else:
    print("El numero ",numero," tiene tres digitos!")