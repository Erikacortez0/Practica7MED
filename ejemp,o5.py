def dividir(a, b):
    if b == 0:
        raise ValueError("No puedes dividir entre cero")
    return a / b

try:
    resultado = dividir(10,0)
except ValueError as e:
    print(e)
else:
    print(resultado)