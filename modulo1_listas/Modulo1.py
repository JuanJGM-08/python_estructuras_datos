Inventario = ["Camisas, 38, 30.00", "Calca, 40, 50.00", "Vestido, 36, 45.00"]

actualizar_precio = "Calca, 40, 50.00"
Inventario[1] = "Calca, 40, 60.00"
# aca se hace la actualizacion del precio de la calca, entramos a la posicion 1 del inventario y la cambiamos por la nueva

def registrar_venta(producto, cantidad): print(f"Hemos vendido: {cantidad} {producto}")
registrar_venta("Camisas", 38 - 35)
# aca lo que se hace es registrar la venta de 3 camisas y se usan 2 print para mostrar el inventario antes y despues de la venta

Inventario.append("Zapatos, 42, 60.00")
# se agrega el nuevo producto al inventario usando el append

print("inventario:", Inventario)
#mostramos inventario 