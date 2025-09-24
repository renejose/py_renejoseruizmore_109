'''
Crea un programa en Python que pida al usuario adivinar un número secreto (por ejemplo, el 7).
al cliente poner mensajes de el numero ingreso es mayor al adivinado 
sino el numero ingresado es menor al adivinado
limitarlo a una cierta cantidad de intentos 

necesito ahora configurar mi juego  
(pedir el nuemro secreto)
(numero de intentos maximos)


menu
========
1) ingresar los valores para configurar
2) que el usuario juegue : 

    que el usuario pueda pedir salir (despues de cada 5 intentos) del juego aun no habiendo completado los numeros de intentos 
    si presionas el numero -1 entonces sale del juego si presionar cualquier otra telca vuelve otra vez al juega.

3) salir de golpe

 * mi programa tiene que pedir que tipo de usaurio es 
si el usuario es adminsitrador entonces puede acceder a todos os menus

si el usaurio es client entonces slo le va a permitir jugar y salir 

'''

def configuracionAdministrador():
    numero_sec =  int(input("ingrese el numero secreto (entre el 1 y el 100)"))
    max_int =   int(input("ingrese el numero maximo de intentos a confgurar"))
    return numero_sec,max_int

def jugar(numero_secreto,max_intentos):
        intentos = 0
        while  intentos <= max_intentos :
            numeroPorAdivinar = int(input("advina el numero secreto ingresando (entre el 1 y el 10)"))
            intentos = intentos + 1 
            
            if intentos % 5 == 0 :
                presionarSalir = int(input("presionar -1 si se desea salir  "))
                if presionarSalir == -1 :
                    print("has presionado -1 y se va salir del juego")
                    opcion = "3"
                    break

            if numeroPorAdivinar == numero_secreto :
                print("adivino")
                break
            elif numeroPorAdivinar > numero_secreto:
                print(" El número ingresado es mayor al número secreto")
            else:
                print(" El número ingresado es menor al número secreto")

            # aviso de intentos restantes
            print(f"Te quedan {max_intentos - intentos} intento(s).")

        if intentos == max_intentos:
            print(f"Se acabaron los intentos. El número secreto era {numero_secreto}.")  


opcion = ""
numero_secreto = 0
max_intentos = 0

while opcion != "3":
    print("Menu de opciones: ")
    print("1) presionar  1 para confgurar el juego")
    print("2) presionar  2 iniciar el juego")
    print("3) presionar  salir")

    opcion = input("elige la opcion :")

    if opcion == "1" :
        # realizar la configuracion
        #configuracionAdministrador()
        numero_secreto ,max_intentos = configuracionAdministrador()

    elif opcion == "2":
        # comenzar a jugar 
        jugar(numero_secreto,max_intentos)
 
    elif opcion == "3":  
        print("se va a cerrar el juego")
        #gracias por jugar  
    else :
        print("el valor que has ingesado como opcion no es valido ")






# numero_secreto =  10 
# # numero_secreto = random.randint(1, 10)
# #numeroPorAdivinar = int(input("advina el numero secreto ingresando (entre el 1 y el 10)"))
# max_intentos = 50

# intentos = 0
# while  intentos <= max_intentos :
#     numeroPorAdivinar = int(input("advina el numero secreto ingresando (entre el 1 y el 10)"))
#     intentos = intentos + 1 
    
#     presionarSalir = int(input("presionar -1 si se desea salir sino continua con el juego presionando 1 "))
#     if presionarSalir == -1 :
#         print("has presionado -1 y se v a salir del juego")
#         break
    


#     if numeroPorAdivinar == numero_secreto :
#         print("adivino")
#         break
#     elif numeroPorAdivinar > numero_secreto:
#         print(" El número ingresado es mayor al número secreto")
#     else:
#         print(" El número ingresado es menor al número secreto")

#     # aviso de intentos restantes
#     print(f"Te quedan {max_intentos - intentos} intento(s).")

# if intentos == max_intentos:
#     print(f"Se acabaron los intentos. El número secreto era {numero_secreto}.")   

 


    # else:
    #     if numeroPorAdivinar > numero_secreto:
    #         print("El número ingresado es mayor al número secreto ")
    #     else:
    #         print("El número ingresado es menor al número secreto.")

    #print("no has acertado")
       
print("hola este codigo pertenece a la version 3")

print("hola este codigo pertenece a la vesion 4")
