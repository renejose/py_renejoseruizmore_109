f = 0
def saludo():
    mensaje = "hola a todos"
    print(mensaje)
    print("bienvenidos al cuso de python")
    f = 10
    k = 9
    if(f == k):
        print("los numero son iguales")
        r = f + k
        if(k != r):
            print("el valor de k es diferente a R")

    print("se finaliza la funcion")    

x =  f
y = 10
saludo()
j = 3
k = j + x
saludo()


puntaje_categoria = 6
ajinomotoactual = 0
totalajinomoto = 20

def hacer_ceviche():
    
    print("hacer cebiche")
    pescado = 4 
    cebolla = 2
    condicionPuntaje = puntaje_categoria
    print("fin de hacer cebiche")
    
def hacer_lomosaltado():
    global totalajinomoto
    print("hacer lomo saltado")
    tomate = 3 
    aji = 2
    lomo = 7
    ajinomoto = 2
    ajinomotoactual = ajinomoto
    condicionPuntaje = puntaje_categoria
    totalajinomoto = totalajinomoto - ajinomotoactual
    print("esta consumiendo ...",ajinomotoactual)
    print("total de animoto que queda" ,totalajinomoto)
    print("fin de lomo saltado")
    
def hacer_lomoderes():
    global totalajinomoto
    print("hacer lomo de res")
    res = 14 
    cebolla = 2
    ajinomoto = 3
    ajinomotoactual = ajinomoto
    condicionPuntaje = puntaje_categoria
    totalajinomoto = totalajinomoto - ajinomotoactual
    print("esta consumiendo ...",ajinomotoactual)
    print("total de animoto que queda" ,totalajinomoto)
    print("fin de hacer lomo de res")
    
    
def hacer_ajigallina():
    print("hacer aji de gallina")
    pollo =4 




