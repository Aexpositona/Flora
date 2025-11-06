#!/usr/bin/env python3
"""
Script para convertir img.png a img.ico
Necesario para PyInstaller
"""

import os
from PIL import Image

def crear_icono():
    try:
        if not os.path.exists('img.png'):
            print("❌ ERROR: img.png no encontrado")
            return False

        img = Image.open('img.png')

        # Redimensionar a múltiples tamaños para mejor compatibilidad
        sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

        # Crear el icono con múltiples tamaños
        img.save('img.ico', format='ICO', sizes=sizes)

        print("✓ Icono creado correctamente: img.ico")
        return True

    except ImportError:
        print("❌ ERROR: Pillow no está instalado")
        print("Instala con: pip install pillow")
        return False

    except Exception as e:
        print(f"❌ ERROR al crear icono: {e}")
        return False

if __name__ == "__main__":
    crear_icono()
