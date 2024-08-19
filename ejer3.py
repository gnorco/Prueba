from PIL import Image
import os
print("Bienvenido")
print("Pegue la ruta de su imagen ")
ruta = input("---> ")
print("Ingrese la rotacion deseada")
rotacion = int(input("---> "))

img = Image.open(ruta)
img2 = img.rotate(rotacion)

img2.show()
lista = ruta.split("/")
print(lista)
extension = img.format
extension.lower()
os.chdir("/home/estudiante/Descargas")
archivo = f"{lista[-1]}OriginalRot.{extension}"
img2.save(archivo)
