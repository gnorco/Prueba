from PIL import Image
import os
print("Bienvenido")
print("Pegue la ruta de su imagen")
ruta = input("---> ")
img = Image.open(ruta)
img.show()
img_copy = img.copy()
os.chdir("/home/estudiante/Descargas")
img_copy.save("img.jpg")