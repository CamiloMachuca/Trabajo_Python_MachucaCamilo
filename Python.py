
import json
from datetime import date
fecha=date.today()
listaProductos=[]
with open("./productos.json", encoding="utf-8") as files:
    listaProductos=json.load(files)

print(listaProductos)

print("########################################################")
print("------------- Gestión de Ventas y Compras -------------")
print("########################################################")
print("(1) Ventas")
print("(2) Compras")
print("(3) Generación de Informes")
opcion=input("Ingresa la opción deseada: ")
if opcion==1:
    print("#########################################")
    print("---------------- Ventas ----------------")
    print("#########################################")
    print("(1) Fecha de venta")
    print("(2) Información del cliente." )
    print("(3) Información del empleado que realizó la venta.")
    print("(4) Productos vendidos")
    opcio=input("Ingrese la opción deseada: ")
    if opcio==1:
        fechaVenta=date.today()


if opcion==1:
    print("#######################################")
    print("---------------- Compras ----------------")
    print("#######################################")
    print("(1) Fecha de la compra.")
    print("(2) Información del proveedor.")
    print("(3) Productos comprados.")
    opci=input("Ingrese la opción deseada: ")
else:
    print("#################################################")
    print("------------ Generación de Informes ------------")
    print("#################################################")
    print("(1) Informes de ventas")
    print("(2) Informes de stock")
    opc=input("Ingrese la opción deseada: ")