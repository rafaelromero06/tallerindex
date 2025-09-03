


def registrar_cliente():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
  
    try:
        with open("clientes.csv", "r", encoding="utf-8") as f:
            next(f)
            ids = [int(linea.split(",")[0]) for linea in f]
            nuevo_id = max(ids) + 1 if ids else 1
    except FileNotFoundError:
        nuevo_id = 1

    with open("clientes.csv", "a", encoding="utf-8") as f:
        f.write(f"{nuevo_id},{nombre},{apellido},{telefono},1\n")
    print("Cliente registrado con éxito.")


def listar_clientes():
    try:
        with open("clientes.csv", "r", encoding="utf-8") as f:
            next(f)
            print("\n Lista de clientes:")
            for linea in f:
                id_cliente, nombre, apellido, telefono, activo = linea.strip().split(",")
                if activo == "1":
                    print(f"ID: {id_cliente} - {nombre} {apellido} ({telefono})")
    except FileNotFoundError:
        print(" No hay clientes registrados.")


def eliminar_cliente():
    id_cliente = input("Ingrese el ID del cliente a eliminar: ")
    lineas = []
    try:
        with open("clientes.csv", "r", encoding="utf-8") as f:
            encabezado = next(f)
            lineas.append(encabezado)
            for linea in f:
                datos = linea.strip().split(",")
                if datos[0] == id_cliente:
                    datos[4] = "0"
                lineas.append(",".join(datos) + "\n")

        with open("clientes.csv", "w", encoding="utf-8") as f:
            f.writelines(lineas)
        print(" Cliente eliminado lógicamente.")
    except FileNotFoundError:
        print(" Archivo de clientes no encontrado.")



def registrar_pedido():
    id_cliente = input("Ingrese el ID del cliente: ")
    producto = input("Producto: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")

    try:
        with open("pedidos.csv", "r", encoding="utf-8") as f:
            next(f)
            ids = [int(linea.split(",")[0]) for linea in f]
            nuevo_id = max(ids) + 1 if ids else 1
    except FileNotFoundError:
        nuevo_id = 1

    with open("pedidos.csv", "a", encoding="utf-8") as f:
        f.write(f"{nuevo_id},{id_cliente},{producto},{precio},{cantidad},1\n")
    print(" Pedido registrado.")


def listar_pedidos_cliente():
    id_cliente = input("Ingrese el ID del cliente: ")
    try:
        with open("pedidos.csv", "r", encoding="utf-8") as f:
            next(f)
            print(f"\n Pedidos del cliente {id_cliente}:")
            for linea in f:
                id_pedido, cliente, producto, precio, cantidad, activo = linea.strip().split(",")
                if cliente == id_cliente and activo == "1":
                    print(f"Pedido {id_pedido}: {producto} - {cantidad} x {precio}")
    except FileNotFoundError:
        print(" No hay pedidos registrados.")



def guardar_venta():
    id_cliente = input("Ingrese el ID del cliente: ")
    producto = input("Producto vendido: ")
    cantidad = int(input("Cantidad: "))
    precio = float(input("Precio : "))
    total = cantidad * precio

    try:
        with open("ventas.csv", "r", encoding="utf-8") as f:
            next(f)
            ids = [int(linea.split(",")[0]) for linea in f]
            nuevo_id = max(ids) + 1 if ids else 1
    except FileNotFoundError:
        nuevo_id = 1

    with open("ventas.csv", "a", encoding="utf-8") as f:
        f.write(f"{nuevo_id},{id_cliente},{producto},{cantidad},{precio},{total}\n")
    print(f"Venta registrada. Total: {total}")


def listar_ventas_cliente():
    id_cliente = input("Ingrese el ID del cliente: ")
    total_final = 0
    try:
        with open("ventas.csv", "r", encoding="utf-8") as f:
            next(f)
            print(f"\n Ventas del cliente {id_cliente}:")
            for linea in f:
                id_venta, cliente, producto, cantidad, precio, total = linea.strip().split(",")
                if cliente == id_cliente:
                    print(f"Venta {id_venta}: {producto} - {cantidad} x {precio} = {total}")
                    total_final += float(total)
        print(f" Total de ventas: {total_final}")
    except FileNotFoundError:
        print(" No hay ventas registradas.")


def menu():
    while True:
        print("\n MENÚ PRINCIPAL ")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Eliminar cliente")
        print("4. Registrar pedido")
        print("5. Listar pedidos de un cliente")
        print("6. Guardar venta")
        print("7. Listar ventas por cliente")
        print("8. Salir")

        opcion = input("Escoja una opción: ")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            listar_clientes()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            registrar_pedido()
        elif opcion == "5":
            listar_pedidos_cliente()
        elif opcion == "6":
            guardar_venta()
        elif opcion == "7":
            listar_ventas_cliente()
        elif opcion == "8":
            print(" Saliendo...")
            break
        else:
            print(" Opción inválida.")


if __name__ == "__main__":
    for archivo, encabezado in [
        ("clientes.csv", "id_cliente,nombre,apellido,telefono,activo\n"),
        ("pedidos.csv", "id_pedido,id_cliente,producto,precio,cantidad,activo\n"),
        ("ventas.csv", "id_venta,id_cliente,producto,cantidad,precio,total\n")
    ]:
        try:
            open(archivo, "r").close()
        except FileNotFoundError:
            with open(archivo, "w", encoding="utf-8") as f:
                f.write(encabezado)

    menu()
