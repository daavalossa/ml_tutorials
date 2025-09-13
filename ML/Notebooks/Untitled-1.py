

archivo = open("C:\\Users\\davalos\\Dropbox\\PC\\Downloads\\APPLOG20220801.txt", "r") # Abre el archivo en modo lectura
contador = {}

for linea in archivo: # Recorre cada línea del archivo
    if linea in contador: # Si la línea ya está en el contador, aumenta su valor en 1
        contador[linea] += 1
    else: # Si la línea no está en el contador, la añade con valor 1
        contador[linea] = 1

archivo.close() # Cierra el archivo

# Muestra las 10 líneas más repetidas
for linea, repeticiones in sorted(contador.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"{repeticiones} veces: {linea}")