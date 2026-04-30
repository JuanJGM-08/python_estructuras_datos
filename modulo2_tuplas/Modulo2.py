catalogo = (
    ("son como niños", "Dennis dugan", 2010, 6.3),
    ("Interstellar", "Christopher Nolan", 2014, 8.6),
    ("Titanes del pacifico", "Guillermo del toro", 2013, 6.9),
    ("King Kong", "Merian C. Gordon y Ernest Schoedsack", 1933, 8.3),
    ("Inception", "Christopher Nolan", 2010, 8.8)
)


# Estaremos mostrando todo el catalogo usando un bucle for para recorrer cada tupla del catalogo 
print("Catálogo Completo")
for titulo, director, anio, puntuacion in catalogo:
    print(f"Película: {titulo} | Director: {director} | Año: {anio} | Score: {puntuacion}")


# separaremos la primera pelicula con el operador *
primera, *_ = catalogo  # el _ lo usaremos para que ignore el resto
print(f"\nPrimera película: {primera[0]}")

# Buscar películas por director
def buscar_por_director(nombre_director):
    encontradas = []
    for peli in catalogo:
        if peli[1] == nombre_director: #el director esta en la posicion 1
            encontradas.append(peli)
    return tuple(encontradas)  # devuelve una tupla con las coincidencias


# Calcular puntuación mínima, máxima y promedio
def obtener_estadisticas():
    puntajes = [peli[3] for peli in catalogo]  # la puntuación está en la posición 3
    minima = min(puntajes)
    maxima = max(puntajes)
    promedio = sum(puntajes) / len(puntajes)
    return minima, maxima, promedio


# Probar la función de búsqueda por director
print("\nPelículas de Christopher Nolan:")
for peli in buscar_por_director("Christopher Nolan"):
    print(f"- {peli[0]}")


# Vamos a desempaquetar las estadisticas de valoracion de mayor a menor
peor, mejor, media = obtener_estadisticas()
print(f"\nEstadísticas: Mínimo = {peor} | Máximo = {mejor} | Promedio = {media:.2f}")