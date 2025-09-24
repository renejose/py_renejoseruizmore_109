'''
caso: leer los 4 primeros bancos de datos de ventas de utiles 


una vez que se haya leido un excel este excel este en una carpeta que se denomine "leidos"

'''
import pandas as pd
import os
import shutil

cantidad = int(input("ingrese la cantidad de archivos excel que deseas leer ? : "))

archivo = input("ingrese el nombre del archivo excel : ")
# Ruta del archivo Excel
contador = 1

if not os.path.exists("leidos"):
    os.makedirs("leidos")

carpeta_reportes = "reportes_ventas_servidor"
while contador <= cantidad:
    archivo_excel = archivo + "_" +str(contador)+".xlsx"  
    #carpeta_leida = os.path.join("leidos")
    if os.path.exists(carpeta_reportes +"/"+archivo_excel):

        # Leer la hoja específica (puedes cambiar el nombre de la hoja)
        df = pd.read_excel(carpeta_reportes +"/"+archivo_excel, sheet_name="Sheet1")

        # Mostrar las primeras filas del archivo
        print(df.head())
        # Mover el archivo a la carpeta "leidos"
        shutil.move(carpeta_reportes +"/"+archivo_excel, "leidos/" + archivo_excel)
        print(f"Archivo {archivo_excel} movido a 'leidos'")
    else :
        print(f"⚠️ El archivo {archivo_excel} no existe.")   
    contador = contador + 1 

print("================= fin de lectura =======================")

