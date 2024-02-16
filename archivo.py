from io import open

archivo_texto=open('anombre.txt', 'r')
#archivo_texto.write("\n datos en el archivo")
#print(archivo_texto.readlines())
#archivo_texto.seek(0)
#print(archivo_texto.read())
#archivo_texto.close()

for lineas in archivo_texto.readlines():
    print(lineas.rstrip())

archivo_texto.close()
