from PIL import Image, ImageDraw, ImageFont
import os
import re
def procesar_imagenes(directorio):
    for raiz, dirs, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith(".jpg") or archivo.endswith(".JPG"):
                nombrearchivo=os.path.splitext(archivo)[0]
                #texto = re.search('10-(.*?)_', nombrearchivo).group(1)
                match = re.search('(10-.*?)_', nombrearchivo)
                if match:
                    texto = match.group(1)
                    print(texto)
                else:
                    texto = "default"
                    print(nombrearchivo) 

                ruta_imagen = os.path.join(raiz, archivo)
                img = Image.open(ruta_imagen)
                
                img_procesada = escribir_texto(aumentar_alto(img, 10), texto)
                img_procesada.save(ruta_imagen)
                print(f"Imagen procesada: {ruta_imagen}")
                
                i = 1
                while os.path.exists(f"{texto}_{i}.jpg"):
                    i += 1
                img_procesada.save(f"{texto}_{i}.jpg")
                
                print(f"Imagen procesada: {texto}_{i}.jpg")








def aumentar_alto(imagen, porcentaje):
    ancho, alto = imagen.size
    nuevo_alto = int(alto * (1 + porcentaje/100))
    nuevo_lienzo = Image.new('RGB', (ancho, nuevo_alto), (255, 255, 255))  # Puedes cambiar el color de fondo si lo deseas
    nuevo_lienzo.paste(imagen, (0, 0))
    nuevo_nombre = "imagen_modificada.jpg"  # Puedes cambiar el nombre según tu preferencia
    nuevo_lienzo.save(nuevo_nombre)
    print(f"Imagen guardada como {nuevo_nombre} con un 10% más de alto.")
    return nuevo_lienzo

def escribir_texto(imagen, texto, color=(0, 0, 0)):
    tamaño_fuente = int(imagen.height * 0.08)
    fuente = ImageFont.truetype("arial.ttf", tamaño_fuente)  # Puedes cambiar la fuente y el tamaño
    dibujo = ImageDraw.Draw(imagen)
    
    # Calcular las coordenadas para centrar el texto
    ancho_texto, alto_texto = dibujo.textsize(texto, font=fuente)
    x = (imagen.width - ancho_texto) / 2
    y = imagen.height * 0.9
    
    dibujo.text((x, y), texto, fill=color, font=fuente)
    imagen.save("imagen_modificada2.jpg")
    return imagen


procesar_imagenes('img')