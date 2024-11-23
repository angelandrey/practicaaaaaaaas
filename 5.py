def suma(lista):
    total = 0
    for num in lista:
        total += num
    return total

def multip(lista):
    total = 1
    for num in lista:
        total *= num
    return total

# Ejemplo:
print(suma([1, 2, 3, 4]))  # Salida esperada: 10
print(multip([1, 2, 3, 4]))  # Salida esperada: 24
