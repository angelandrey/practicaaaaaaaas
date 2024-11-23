def max_de_tres(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# Ejemplo:
print(max_de_tres(5, 10, 7))  # Salida esperada: 10
