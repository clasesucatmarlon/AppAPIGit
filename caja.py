#-*- coding: utf-8-*-
import sys

articulos={}
fulltotal=0
def ingreso_productos():
    caja=True
    while caja==True:
        opcion =input("Va a ingresar un artículo SI/NO: ")
        try:
            if opcion.isalpha()==True:
                if opcion.lower()=="si":
                    producto=input("ingrese el articulo: ")
                    precio=int(input("ingrese el precio: "))
                    articulos[producto]=precio
                elif opcion.lower()=="no":
                    caja=False
                else:
                    print("información no reconocida")
            else:
                print("no se reconocen datos numericos")
        except:
            caja=True
    print("sus articulos existentes son: ")
    for clave in articulos:
        print(clave,":",articulos[clave])


#  Cliente*************
#  ********************************************
def compras():
	if len(articulos)>0:
	    caja_2=True
	    total=0
	    while caja_2==True:
	        for clave in articulos:
	        	print(clave,":",articulos[clave])
	        producto=input("Qué artículos va a llevar: ")
	        for elemento in articulos:
	            if elemento==producto:
	                print("usted eligió %s"%(elemento))
	                cantidad=input("qué cantidad desea llevar del producto: ")
	                cantida=cantidad*articulos[elemento]
	                total=total+cantida
	                
	                print("articulo %s: cantidad %s: subtotal de factura Q.%s "%(elemento, cantidad,total ))
	                volver=True
	                while volver==True:
	                    seguir=input("quiere elegir otro articulo SI/NO: ")
	                    if seguir.lower()=="si":
	                        caja_2=True
	                        volver=False
	                    elif seguir.lower()=="no":
	                        caja_2=False
	                        volver=False
	                        return total
	                    else:
	                        print("opcion invalida")
	                        volver=True
	else:
		print("No hay productos en existencia")


#  Factura*****************
#  ***************************************************
def factura():
    caja_2=True
    while caja_2==True:
        print("1.Master")
        print("2.Visa")
        print("3.Ninguna")
        tarjeta=input("Elija el tipo de tarjeta?: ")
        try:
            if tarjeta.isalpha()==False:
                # INGRESO PRODUCTO 
                #*******************************************************
                if tarjeta=="1":
			        print("Master")
					print("Tiene un descuento del 5%:")
					print("El subtotal de la factura esQ.%s"%(fulltotal))
					IVA = (fulltotal*0.12)
					descuento = (fulltotal*0.05)
					totaltotal = fulltotal + IVA - descuento
					#  comienza facturación
					print("Debe: %s"%(fulltotal))
					print("______________________")
					nombre_del_cliente = input("Nombre Del Cliente: ")
					nit = input("NIT: ")
					efectivo = input("Efectivo :  ")
					cambio = efectivo - fulltotal
					print("__________________________")
					print(("Precio       %.2f\t") % fulltotal)
					print( ("IVA          %.2f\t") % IVA)
					print(("Total        %.2f\t") % totaltotal)
					print(("Efectivo     %.2f\t") % efectivo)
					print("__________________________")
					print("cambio:   %s"%(cambio))
					break
                # COMPRA
                #*******************************************************************
                elif tarjeta=="2":
                    print("Visa")
                    print("Tiene un descuento del 2%:")
                    print("El subtotal de la factura esQ.%s"%(fulltotal))
                    IVA = (fulltotal*0.12)
                    descuento = (fulltotal*0.02)
                    totaltotal = fulltotal + IVA - descuento
                    #  comienza facturación
                    print("Debe: ",totaltotal)
                    print("______________________")
                    nombre_del_cliente = input("Nombre Del Cliente: ")
                    nit = input("NIT: ")
                    efectivo = input("Efectivo :  ")
                    cambio = efectivo - totaltotal
                    print("__________________________")
                    print(("Precio       %.2f\t") % fulltotal)
                    print(("IVA          %.2f\t") % IVA)
                    print(("Total        %.2f\t") % totaltotal)
                    print(("Efectivo     %.2f\t") % efectivo)
                    print("__________________________")
                    print(("cambio:   "),cambio)
                    caja_2=False
                elif tarjeta =="3":
                    IVA = (fulltotal*0.12)
                    totaltotal = fulltotal + IVA 
                    #  comienza facturación
                    print("Debe: ",totaltotal)
                    print("______________________")
                    nombre_del_cliente = input("Nombre Del Cliente: ")
                    nit = input("NIT: ")
                    efectivo = input("Efectivo :  ")
                    cambio = efectivo - totaltotal
                    print("__________________________")
                    print(("Precio       %.2f\t") % fulltotal)
                    print(("IVA          %.2f\t") % IVA)
                    print(("Total        %.2f\t") % totaltotal)
                    print(("Efectivo     %.2f\t") % efectivo)
                    print("__________________________")
                    print(("cambio:   "),cambio)
                    caja_2=False
                else:
                    print("opcion no valida")
            else:
                print("Debe ingresar cantidades no se permiten letras ni caracteres especiales")
        except:
            opcion3=True
	print("Gracias por su compra, hasta la próxima")


#  Menu************************
#  ***********************************************
salir=False
while salir==False:
    print("Caja Registradora")
    print("¿Qué desea realizar?")
    print("1. Ingreso productos")
    print("2. Compras")
    print("3. Factura")
    opmenu = input("ingrese opción: ")
    try:
	    if opmenu.isalpha()==False:
		    if opmenu =="1":
		        ingreso_productos()
		        opcionmenu=input("Desea volver al menu SI/NO: ")
		        if opcionmenu.lower()=="si":
		        	salir=False
		        else:
		            break
		    elif opmenu =="2":

		        fulltotal= compras()
		        print(fulltotal)
		        opcionmenu=input("Desea volver al menu SI/NO: ")
		        if opcionmenu.lower()=="si":
		            salir=False
		        else:
		            break
		    elif opmenu =="3":
		        print(factura())
		        opcionmenu=input("Desea vover al menu SI/NO: ")
		        if opcionmenu.lower()=="si":
		            salir=False
		        else:
		            break
    except:
		print("Adios")