#!/usr/bin/env python3
"""
Script para convertir img.png a img.ico
Necesario para PyInstaller
"""

import os
from PIL import Image

def crear_icono():
    try:
        # Buscar img.png en assets/images/
        img_path = os.path.join('assets', 'images', 'img.png')
        if not os.path.exists(img_path):
            print(f"❌ ERROR: {img_path} no encontrado")
            return False

        img = Image.open(img_path)

        # Redimensionar a múltiples tamaños para mejor compatibilidad
        sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

        # Crear el icono en assets/icons/
        ico_path = os.path.join('assets', 'icons', 'img.ico')
        os.makedirs(os.path.dirname(ico_path), exist_ok=True)
        img.save(ico_path, format='ICO', sizes=sizes)

        print(f"✓ Icono creado correctamente: {ico_path}")
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
