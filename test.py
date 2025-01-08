from os import system
system ("cls")

#EJERCICIO 1

# nombre="Emilio Parra"
# edad=18
# print("mi nombre es ",nombre," mi edad es ",edad)


#EJERCICIO 2
# num1=int(input("ingrese un número \n "))
# num2=int(input("ingrese otro número \n"))
# print(num1+num2)


#EJERCICIO 3
# num1=int(input("ingrese un número \n "))

# if num1 > 0:
#     print("El numero es positivo")
# else:
#     print("El numero es negativo o cero")


#EJERCICIO 4
# edad=int(input("ingrese su edad"))

# if edad >= 18:
#     print("usted es mayor de edad")
# else:
#     print("usted es menor de edad")


#EJERCICIO 5
# num1=int(input("ingrese un número \n "))
# num2=int(input("ingrese un número \n "))
# num3=int(input("ingrese un número \n "))
    
# print(f"su promedio es {(num1+num2+num3)/3}")


#EJERCICIO 6
# cantidadentradas=int(input("ingrese cuantas entradas va a comprar \n "))
# valor=0

# for i in range(cantidadentradas):
#     edad=int(input("ingrese su edad \n "))

#     if edad<=12:
#         print("usted debe pagar $500")
#         valor+=500
#     else:
#         if edad >= 13 and edad <= 18:
#             print("usted debe pagar $1000")
#             valor+=1000
#         else:
#             if edad >= 19 and edad <= 64:
#                 print("usted debe pagar $2000")
#                 valor+=2000
#             else:
#                 print("usted debe pagar $700")
#                 valor+=700
    
# print(f"su total es {valor}")


#EJERCICIO 7
# ubi=input("¿pertenece a la florida? \n")

# monto=5000
# if ubi =="si":
#     print("continuando...")
#     opc1=input("tiene carnet socio? \n").lower()
#     if opc1 == "si":
#         numc=int(input("ingrese su numero de carnet \n"))
#         jubi=input("¿Es jubilado? \n").lower()
#         if jubi == "si":
#             print(f" su monto a pagar es {monto*0.75} que cuenta con un 25% de descuento")
#         else:
#             print(f"usted debe pagar el siguente monto: {monto} ")
#     else:
#         nom=input("ingresa tu nombre \n")
#         rut=int(input("ingresa tu rut sin puntos y sin (-) \n"))
#         telefono=int(input("ingresa tu numero de celular \n"))
#         print("carnet creado")
#         jubi=input("¿Es jubilado? \n").lower()
#         if jubi == "si":
#             print(f" su monto a pagar es {monto*0.75} que cuenta con un 25% de descuento")
#         else:
#             print(f"usted debe pagar el siguente monto: {monto} ")
            
# else:
#     print("Gracias por visitar")  

