def crear_factura(productos):
    # Cabecera de la factura
    print("\n" + "=" * 40)
    print("{:^40}".format("FACTURA"))
    print("=" * 40)
    print("{:<20} {:>5} {:>7} {:>7}".format("Producto", "Cant.", "Precio", "Total"))
    print("-" * 40)

    # Cuerpo de la factura
    total_general = 0
    for producto in productos:
        nombre = producto['nombre']
        cantidad = producto['cantidad']
        precio = producto['precio']
        total = cantidad * precio
        total_general += total
        
        print("{:<20} {:>5} ${:>6.2f} ${:>6.2f}".format(nombre[:20], cantidad, precio, total))

    # Pie de la factura
    print("-" * 40)
    print("{:>32} ${:>6.2f}".format("Total General:", total_general))
    print("=" * 40)

# Lista para almacenar los productos
productos = []

# Ingreso de productos
while True:
    nombre = input("Ingrese el nombre del producto (o presione Enter para terminar): ")
    if nombre == "":
        break
    
    cantidad = int(input("Ingrese la cantidad: "))
    precio = float(input("Ingrese el precio unitario: "))
    
    productos.append({
        'nombre': nombre,
        'cantidad': cantidad,
        'precio': precio
    })

# Crear y mostrar la factura
crear_factura(productos)