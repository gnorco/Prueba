from PIL import Image
import os 


while (True):
    ruta_img = input("ingrese la ruta de la imagen ---> ")
    img = Image.open(ruta_img)
    print(img.size)
    left = int(input("Ingrese el valor para recortar en la parte izquierda ---> "))
    upper = int(input("Ingrese el valor para recortar en la parte superior ---> "))
    right = int(input("Ingrese el valor para recortar en la parte derecha ---> "))
    lower = int(input("Ingrese el valor para recortar en la parte inferior ---> "))
    while left > right or upper > lower:
        print("Los valores que ha ingresado no son validos. Por favor ingreselos nuevamente")
        left = int(input("Ingrese el valor para recortar en la parte izquierda ---> "))
        upper = int(input("Ingrese el valor para recortar en la parte superior ---> "))
        right = int(input("Ingrese el valor para recortar en la parte derecha ---> "))
        lower = int(input("Ingrese el valor para recortar en la parte inferior ---> "))
    
    img_cropped= img.crop((left,upper,right,lower))
    carpeta= "recortes"
    os.chdir("/home/estudiante/Descargas")
    if not os.path.exists(carpeta):
        os.mkdir(carpeta)
    contador = 1
    while True:
        archivo = f"img{contador}.png"
        ruta_archivo = os.path.join(carpeta, archivo)
        if not os.path.exists(ruta_archivo):
            break
        contador += 1

    img_cropped.save(ruta_archivo)
    print("El archivo se guardo con exito")
    img_cropped.show()
    break