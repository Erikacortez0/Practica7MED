try:
    valor = int(input("Ingrese un numero: "))
    resultado = 10 / valor
except ValueError:
    print("Error : debe ingresar un numero valido")
except ZeroDivisionError:
    print("Error: no se puede dividir entre 0")
else:
    print(f"El resultado es {resultado}")