# Cómo usar generar_exe.bat

## Requisitos previos
- Python 3.9+ instalado
- Archivo `main.py` presente
- Archivo `plantas.json` presente  
- Archivo `img.png` presente (para el icono)

## Archivos necesarios (ya incluidos)
- `crear_icono.py` - Convierte img.png a img.ico
- `version_info.txt` - Metadatos del ejecutable
- `INSTRUCCIONES_PRIMERA_VEZ.txt` - Guía para usuarios
- `SOLUCIONES_ANTIVIRUS.md` - Soluciones para alertas

## Ejecutar el script
1. Haz doble clic en `generar_exe.bat`
2. El script detectará automáticamente Python
3. Instalará dependencias (pillow, pyinstaller)
4. Creará el icono desde img.png
5. Compilará el ejecutable
6. Creará la carpeta `flora/` con todo
7. Generará `JuegoPlantas.zip` para distribución

## Resultado final
- Carpeta `flora/` con el juego completo
- Archivo `JuegoPlantas.zip` listo para compartir

## Solución de problemas
- Si falla: Verificar que Python está en PATH
- Si no encuentra archivos: Ejecutar desde la carpeta raíz del proyecto
- Para más ayuda: Ver los mensajes del script
