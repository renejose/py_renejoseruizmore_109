#estructura de datos dinamicas 
#Listas, Tuplas , Diccionarios , Conjuntos
# 
#estructuraLista = [2,1,4,5,8,7,9,6,5,8,12,4,5,8,7,9]
#cantidadDatos = estructuraLista.__len__()
# ====================== recorrer el listado ==============================
# i = 0 
# while i < cantidadDatos:
#     print(estructuraLista[i])
#     i +=  1 # i = i + 1

# for item in estructuraLista :
#     print(item)

# print("el valor maximo de la estructura es: ",max(estructuraLista))
# print("el valor mainimo de la estructura es: ",min(estructuraLista))
# print("la asumatoria es: ",sum(estructuraLista))

#======================== fin de recorrido ==========================

# Tupla = (1,5,6,4,59,8,7,45)
# Conjunto = {1,2,3,6,5,4,9}
# Diccionario = { "nombre" : "Juan Perez", "edad" : 45 , "nacionalidad" : "peruana" }

#Lista
# numeros = [140,20,90,40,50,95,100]

# numeros.append(95)
# numeros.append(100)
# numeros.append(180)

# cantidadDatos = numeros.__len__()
# print(cantidadDatos)
# print(numeros)
# ultimo = numeros.pop()
# #print(ultimo)

# numeros.sort()
# print(numeros)



# indice = 0

# while(indice < cantidadDatos ):
#     print(numeros[indice])
#     indice = indice + 1

#numeros.remove(20)


#tuplas 
# colores = ("azul","rojo","amarillo", "azul", "verde","rojo", "rojo")
# #cantidad de elementos que se repiten 
# valoresRepetidos = colores.count("azul")
# inidice = colores.index("rojo")
# print(inidice) 
# for color in colores:
#     print(color)

# conjuntos 
# conjuntoA = {1,2,3,6,5,4,9,9,9,9,9,9,9,99,9,99,99,9,99,8,7,1,2,3}

# conjuntoB = {2,3,16,19,18}

# for elemento in conjunto:
#     print(elemento)


#print(conjuntoA.union(conjuntoB))
#print(conjuntoA.intersection(conjuntoB))
#print(conjuntoA.difference(conjuntoB))


# estructuraLista = [2,1,4,5,8,7,9,6,5,8,12,4,5,8,7,9]

# conjunto = set(estructuraLista)
# print(conjunto)


# productos = ["manzanas", "leche","pan" , "leche","pan", "peras"]

# productos_unicos = set(productos)
# print(productos_unicos)


#======================== diccionario ========================

# key 
#Value


persona1 = { 
                "nombre" : "Juan Perez", 
               "edad" : 45 , 
               "nacionalidad" : "peruana" }

persona2 = { 
                "nombre" : "Rene Jose", 
               "edad" : 32 , 
               "nacionalidad" : "peruana" }

persona3 = { 
               "nombre" : "Jose Velarde", 
               "edad" : 62 , 
               "nacionalidad" : "peruana" }


persona1["nombre"] = "Pedro Paulet"

#print(persona1["nombre"])

persona1.pop("edad")

persona1.update({"fechaNacimiento": "18-05-1993"})

print(persona1)















