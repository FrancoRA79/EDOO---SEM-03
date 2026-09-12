print("Uso de la listas simplemente enlazadas")

def buscar_producto(productos, nombre):
    for producto in productos:
        if producto["nombre"] == nombre:
            return producto

    return None

print("Comprobando el push")
print("Comprobando de nuevo")