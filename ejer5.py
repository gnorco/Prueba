from PIL import Image
import os 
print("Bienvenido")
print("Ingrese una ruta de una imagen")
ruta_img = input("---> ")
print("Ingrese la ruta de la marca de agua")
ruta_marca_agua = input("---> ")

img = Image.open(ruta_img)
marca_agua = Image.open(ruta_marca_agua)
margen = 50
print("Donde desea establecer la marca de agua")
print("1 - Parte superior izquierda")
print("2 - Parte superior derecha")
print("3 - Parte inferior izquierda")
print("4 - Parte inferior derecha")
posicion = int(input("Ingrese un numero  ---> "))

img_new = img.copy()

while posicion != 1 and posicion != 2 and posicion != 3 and posicion != 4:
    print("El numero que ha ingresado es incorrecto \n Por favor Ingrese otro numero")
    print("1 - Parte superior izquierda")
    print("2 - Parte superior derecha")
    print("3 - Parte inferior izquierda") 
    print("4 - Parte inferior derecha") 
    posicion = int(input("---> "))

if marca_agua.mode != "RGBA":
    marca_agua = marca_agua.convert("RGBA")

alpha_mask = marca_agua.split()[3]
if posicion == 1:
    img_new.paste(marca_agua, (margen,margen))
elif posicion == 2:
    posX = img_new.width - margen - marca_agua.width
    img_new.paste(marca_agua, (posX,margen), mask= alpha_mask)
elif posicion == 3 :
    posY = img_new.height - margen - marca_agua.height
    img_new.paste(marca_agua, (margen, posY), mask = alpha_mask)
else:
    posX = img_new.width - margen - marca_agua.width
    posY = img_new.height - margen - marca_agua.height
    img_new.paste(marca_agua, (posX, posY), mask=alpha_mask)

os.chdir("/home/estudiante/Descargas/")
archivo = "marca_de_agua.jpg"
img_new.save(archivo)
print(f'La imagen se ha guardado con exito')
img_new.show()
