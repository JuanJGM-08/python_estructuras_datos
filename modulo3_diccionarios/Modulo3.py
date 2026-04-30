ventas_por_region = {
    "Norte": {"Q1": 30000, "Q2": 35000, "Q3": 12000, "Q4": 25000},
    "Sur": {"Q1": 19000, "Q2": 21000, "Q3": 15000, "Q4": 19000},
    "Este": {"Q1": 25000, "Q2": 27000, "Q3": 28000, "Q4": 26000},
    "Oeste": {"Q1": 14000, "Q2": 13000, "Q3": 15000, "Q4": 14000}
}
# Cada region tiene un diccionario con las ventas por trimestre (Q1, Q2, Q3, Q4)

# 2 Calcula el total anual de cada región: aca calculamos el total anual de cada región sumando los valores de los trimestres
totales_regionales = {}
for region, trimestres in ventas_por_region.items():
    totales_regionales[region] = sum(trimestres.values())

# 3. Usa max() con key=lambda para la región con mayores ventas; usamos max() para encontrar la region con mayores ventas y el "lambda" para especificar lo que compararemos
mejor_region = max(totales_regionales.items(), key=lambda x: x[1])

# 4. Acumula ventas por trimestre con iteración anidada: un diccionario para acumular las ventas por trimestre, iteramos la region y luego trimestre
ventas_trimestrales = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
for trimestres in ventas_por_region.values():
    for trimestre, monto in trimestres.items():
        ventas_trimestrales[trimestre] += monto

# 5. Genera porcentajes con dict comprehension sobre el gran total: sumando los totales regionales y luego un comprension para calcular el porcentaje de cada region
gran_total = sum(totales_regionales.values())
porcentajes = {region: round((total / gran_total) * 100, 2)
               for region, total in totales_regionales.items()}

# 6. Reporte ordenado de mayor a menor ventas
print("REPORTE DE VENTAS POR REGIÓN")
reporte = sorted(totales_regionales.items(), key=lambda x: x[1], reverse=True)

for region, total in reporte:
    print(f"Región: {region:6} | Total: ${total:7} | Participación: {porcentajes[region]}%")
print(f"\nRegión con mayores ventas: {mejor_region[0]} (${mejor_region[1]})")