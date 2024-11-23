def es_vocal(c):
    if len(c) != 1:  # Asegura que sea solo un carácter
        return False
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return c in vocales

# Ejemplo:
print(es_vocal("a"))  # Salida esperada: True
print(es_vocal("b"))  # Salida esperada: False
