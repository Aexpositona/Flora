import os
import shutil

IMAGENES_DIR = "flora/imagenes"

def copiar_imagenes_planta(nombre_cientifico, rutas_imagenes):
    nombre_limpio = "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in nombre_cientifico)
    nombre_limpio = nombre_limpio.replace(' ', '_')

    carpeta_planta = os.path.join(IMAGENES_DIR, nombre_limpio)
    os.makedirs(carpeta_planta, exist_ok=True)

    rutas_locales = []
    for ruta_original in rutas_imagenes:
        if os.path.exists(ruta_original):
            nombre_archivo = os.path.basename(ruta_original)
            ruta_destino = os.path.join(carpeta_planta, nombre_archivo)

            contador = 1
            nombre_base, extension = os.path.splitext(nombre_archivo)
            while os.path.exists(ruta_destino):
                nombre_archivo = f"{nombre_base}_{contador}{extension}"
                ruta_destino = os.path.join(carpeta_planta, nombre_archivo)
                contador += 1

            shutil.copy2(ruta_original, ruta_destino)
            rutas_locales.append(ruta_destino)
        else:
            rutas_locales.append(ruta_original)

    return rutas_locales

def eliminar_carpeta_planta(nombre_cientifico):
    nombre_limpio = "".join(c if c.isalnum() or c in (' ', '_') else '_' for c in nombre_cientifico)
    nombre_limpio = nombre_limpio.replace(' ', '_')

    carpeta_planta = os.path.join(IMAGENES_DIR, nombre_limpio)
    if os.path.exists(carpeta_planta):
        try:
            shutil.rmtree(carpeta_planta)
        except Exception as e:
            print(f"Error al eliminar carpeta: {e}")

def crear_directorio_imagenes():
    os.makedirs(IMAGENES_DIR, exist_ok=True)

