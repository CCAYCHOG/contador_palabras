#Importar librerías
from collections import Counter

while True:
    # Definir el conjunto de palabras vacías
    palabrasvacias = {"el", "la", "los", "las", "un", "una", "unos", "unas", 
             "y", "o", "de", "del", "a", "en", "con", "por", "para", 
             "es", "al", "se", "que", "lo", "su", "sus", "como"}
    
    # Introducción un texto por parte del usuario
    texto = input("Introduce un texto: ")

    # Caracteres no deseados a eliminar
    caracteres_a_remover = ".,;:!?¿¡()[]{}\"'"

    # Eliminar caracteres no deseados y convertir a minúsculas
    for caracter in caracteres_a_remover:
        texto = texto.replace(caracter, "")

    # Separar el texto en palabras y eliminar las palabras vacías
    palabras = texto.lower().split()

    # Filtrar las palabras vacías
    palabras_filtradas = [palabra for palabra in palabras if palabra not in palabrasvacias]

    # Contar las palabras
    contador = Counter(palabras_filtradas)

    # Mostrar el resultado
    print("Contador de palabras:")
    for palabra, cantidad in contador.items():
        print(f"{palabra}: {cantidad}")