# 1 Define tienda_centro, tienda_norte y tienda_sur como sets de productos (Completado)
tienda_centro = {"Monitor", "Teclado", "Mouse", "Laptop"}
tienda_norte = {"Teclado", "Webcam", "Laptop", "Microfono"}
tienda_sur = {"Monitor", "Impresora", "Mouse", "Laptop"}

# 2 Calcula catalogo_completo con union() y productos_comunes con intersection() usamos el union para obtener el catalogo completo
catalogo_completo = tienda_centro.union(tienda_norte, tienda_sur)
# los productos que se venden en todas las tiendas (intersección)
productos_comunes = tienda_centro.intersection(tienda_norte, tienda_sur)

# 3 Usa difference() para exclusivos de cada tienda e isdisjoint() para solapamientos, se usa isdisjoint para productos que se venden en 2 tiendas y difference para exclusivos de 1 tienda
solo_centro = tienda_centro.difference(tienda_norte | tienda_sur)
solo_norte = tienda_norte - (tienda_centro | tienda_sur)
solo_sur = tienda_sur - (tienda_centro | tienda_norte)

# Verificar si alguna de las tiendas no tienen productos en común (isdisjoint)
sin_relacion = tienda_norte.isdisjoint(tienda_sur)

# Preferencias de películas por género (conjuntos)
usuario1 = {"Accion", "Drama", "Sci-Fi"}
usuario2 = {"Drama", "Romance", "Comedia"}
usuario3 = {"Sci-Fi", "Accion", "Aventura"}

# Operadores con conjuntos: & = intersección, | = unión, < = subconjunto
comunes_1_2 = usuario1 & usuario2
universo_cine = usuario1 | usuario2 | usuario3
# Verificar si usuario3 es un subconjunto del universo de gustos
es_subgrupo = usuario3 < universo_cine

# Mostrar el resultado de los cálculos
print(f"Total productos únicos: {len(catalogo_completo)}")
print(f"Productos en todas las sucursales: {productos_comunes}")
print(f"Exclusivo Centro: {solo_centro}")
print(f"¿Norte y Sur no comparten nada?: {sin_relacion}")
print(f"Gustos comunes User 1 y 2: {comunes_1_2}")
print(f"¿User 3 está dentro del universo?: {es_subgrupo}")