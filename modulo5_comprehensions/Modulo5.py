# Acá armamos todo el cálculo de ventas: valor total, productos top, ranking de caros, cosas baratas y el gran total final
ventas = [
    {"prod": "Laptop", "uds": 5, "precio": 1200, "cat": "Tech"},
    {"prod": "Mouse", "uds": 50, "precio": 25, "cat": "Accesorios"},
    {"prod": "Monitor", "uds": 10, "precio": 300, "cat": "Tech"},
    {"prod": "Teclado", "uds": 20, "precio": 75, "cat": "Accesorios"},
    {"prod": "USB", "uds": 100, "precio": 10, "cat": "Accesorios"}
]

# 1. List comprehension: valor total (unidades × precio) por cada producto
valores_totales = [v["uds"] * v["precio"] for v in ventas]

# 2. List comprehension con filtro: productos con valor_total > 1000
productos_destacados = [v["prod"] for v in ventas if (v["uds"] * v["precio"]) > 1000]

# 3. Dict comprehension: mapea nombre → {valor_total, unidades}
producto_info = {v["prod"]: {"valor": v["uds"] * v["precio"], "unidades": v["uds"]} for v in ventas}

# 4. Dict comprehension con filtro: ranking_premium (precio > 50) ordenado por valor descendente
ranking_premium = dict(sorted(
    {v["prod"]: v["uds"] * v["precio"] for v in ventas if v["precio"] > 50}.items(),
    key=lambda x: x[1],
    reverse=True
))

# 5. Set comprehension: categorías únicas y productos baratos (precio ≤ 50)
categorias_unicas = {v["cat"] for v in ventas}
productos_baratos = {v["prod"] for v in ventas if v["precio"] <= 50}

# 6. Combinar todo: resumen formateado + gran total con sum()
gran_total = sum(valores_totales)

# Reporte final
print(f"Categorías encontradas: {categorias_unicas}")
print(f"Productos de alto valor (>1000): {productos_destacados}")
print(f"Ranking Premium (de mayor a menor): {ranking_premium}")
print(f"Productos económicos (precio ≤ 50): {productos_baratos}")
print(f"TOTAL GENERAL DE VENTAS: ${gran_total}")