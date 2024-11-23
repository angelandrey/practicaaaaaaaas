def es_palindromo(palabra):
    return palabra == palabra[::-1]

# Ejemplo:
print(es_palindromo("radar"))  # Salida esperada: True
print(es_palindromo("python"))  # Salida esperada: False
