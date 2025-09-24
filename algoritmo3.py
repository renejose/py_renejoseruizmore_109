def dividir(a,b):
    try:
        z = a/b
        print("la division es:" , z)
    except ZeroDivisionError:
        print("la division es indeterminada") 
    except Exception as e:
        print("ocurio un problema") 
             
    

def abrir_archivo(nombre):
    try:
        archivo= open(nombre,"r")
        contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        print("Error : el archivo no existe en mi disco") 



dividir(17,0)
