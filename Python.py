
import json

from datetime import date

listaProductos=[]
with open("./productos.json", encoding="utf-8") as files:# se crea una función para extraer los datos del json
    listaProductos=json.load(files)

listaventas=[]
with open("./ventas.json", encoding="utf-8") as files:# se crea una función para extraer los datos del json
    listaventas=json.load(files)
     


compras=[]
with open("./compras.json", encoding="utf-8") as files:# se crea una función para extraer los datos del json
    compras = json.load(files)



def guardarArchivo(archivo,datos):# Se crea una función que permite guardar todos los cambios en los json 
    with open(archivo,"w", encoding="utf-8") as outfile:
        json.dump(datos,outfile, indent=4)

def Guaedarrcompra(id,fecha,nombreProveedor,contacto_provedor,productos):# Se crea una función para guardar las compras en el json 
    compra={
        "id":id,
        "fecha":fecha,
        "Información del proveedor":{
            "nombre": nombreProveedor,
            "contacto":contacto_provedor
        },
        "productos":[]
    }
    for producto,cantidad,precio in productos:
        compra["productos"].append({
            "nombre": producto,
            "cantidad":cantidad,
            "precioCompra": precio
        })
    compras.append(compra)
    guardarArchivo("compras.json",compras)

def Guardarventa(id,fecha,nombreCliente,direccionCliente,nombreEmpleado,cargoEmpleado,productos):# se crea una función para guardar las ventas realizadas en el json
    venta={
        "id":id,
        "fecha":fecha,
        "InformaciónCliente":{
            "nombre": nombreCliente,
            "direccion": direccionCliente
        },
        "productosVendidos":[],
        "empleado":{
            "nombre": nombreEmpleado,
            "cargo": cargoEmpleado
        }
    }
    for producto,cantidad,precio in productos:
        venta["productosVendidos"].append({
            "nombre": producto,
            "cantidad":cantidad,
            "preciodeventa": precio
        })
    listaventas.append(venta)
    guardarArchivo("ventas.json",listaventas)

menuu=True
while menuu==True:
    print("########################################################")
    print("------------- Gestión de Ventas y Compras -------------")# Se crea el menu principal el cual cuenta con 4 opciones 
    print("########################################################")
    print("(1) Ventas")
    print("(2) Compras")
    print("(3) Generación de Informes")
    print("(4) Finalizar programa")
    opcion=int(input("Ingresa la opción deseada: "))
    if opcion==1:
        print("#########################################")
        print("---------------- Ventas ----------------")
        print("#########################################")
        id=len(listaventas)+1
        fechaVenta=str(date.today())
        nombreCliente=input("nombre del cliente: ")
        direccionCliente=input("Direccion del cliente: ")
        nombreEmpleado=input("Nombre del empleado: ")
        cargoEmpleado=input("Cargo del empleado: ")
        productos=[]
        buliano=True
        while buliano==True:# se utiliza un bucle while para crear los productos que el usuario requiera y asi añadirlos al json
            producto=input("escribe el nombre del producto: ")
            cantidad=int(input("cantidad: "))
            precio=str(input("Precio: "))
            productos.append((producto, cantidad, precio))
            seguir=int(input("si deseas agregar otro producto escribe (si=1) o si deseas finalizar escribe (no=2)"))
            if seguir==1:
                buliano=True
            elif seguir==2:
                buliano=False
        Guardarventa(id,fechaVenta, nombreCliente, direccionCliente, nombreEmpleado, cargoEmpleado,productos)



    elif opcion==2:# Se realiza la opción 2 del menu principal
        print("#######################################")
        print("---------------- Compras ----------------")
        print("#######################################")
        
        id=len(compras)+1
        fecha=str(date.today())
        nombreProveedor=input("nombre del proveedor: ")
        contactoProveedor=input("Escribe el contacto del proveedor: ")
        productos=[]
        buliano=True

        while buliano==True: # se utiliza un bucle while para crear los productos que el usuario requiera y asi añadirlos al json
            producto=input("escribe el nombre del producto: ")
            cantidad=int(input("cantidad: "))
            precio= float(input("precio de compra: "))
            productos.append((producto,cantidad,precio))
            seguir=int(input("si deseas agregar otro producto escribe (si=1) o si deseas finalizar escribe (no=2)"))
            if seguir==2:
                break
        Guaedarrcompra(id,fecha, nombreProveedor, contactoProveedor,productos)




    elif opcion==3:# se crea la opción 3 del menu principal

        print("#################################################")
        print("------------ Generación de Informes ------------")
        print("#################################################")
        print("(1) Informes de ventas")
        print("(2) Informes de stock")
        opc=int( input("Ingrese la opción deseada: "))

        if opc==1:
            print("##############(1) Informes de ventas ##################")
            print()
            for venta in listaventas:# se utiliza un bucle for para que recorra la lista de ventas y asi imprima todos los datos de esta lista
                print()
                print("ID: ", venta.get("id", "No disponible"))
                print("Fecha: ", venta.get("Fecha", venta.get("fecha", "No disponible")))
                
                # Información del cliente
                cliente = venta.get("InformacionCliente", venta.get("InformaciónCliente", {}))
                print("Cliente: ", cliente.get("nombreCliente", cliente.get("nombre", "No disponible")))
                print("Dirección: ", cliente.get("direccion", "No disponible"))
                
                # Información del empleado
                empleado = venta.get("Empleado", venta.get("empleado", {}))
                print("Empleado: ", empleado.get("nombreEmpleado", empleado.get("nombre", "No disponible")))
                print("Cargo: ", empleado.get("cargoEmpleado", empleado.get("cargo", "No disponible")))
                
                # Productos vendidos
                productos = venta.get("Productosvendidos", venta.get("productosVendidos", []))
                for producto in productos:
                    print("Producto: ", producto.get("nombre", "No disponible"))
                    print("Cantidad: ", producto.get("cantidad", "No disponible"))
                    print("Precio de venta: ", producto.get("preciodeventa", producto.get("precioVenta", "No disponible")))




        elif opc==2:
            print("##############(1) Informes de stock ##################")
            for categoria, productos in listaProductos.items():
                print()
                print(f"Categoria:{categoria}")
                print()
                for producto, precio in productos.items():
                    print(f"  producto: {producto}--------------- Precio:{precio}")
                
    else:
        menuu=False

# Proyecto desarrollado por Camilo Machuca Vega Grupo: T2