# 🌱 Flora Game - Juego Educativo de Plantas

[![Licencia: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Educativo](https://img.shields.io/badge/Tipo-Educativo-green.svg)]()
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)]()

## 📚 Descripción

**Flora Game** es una aplicación educativa opensource diseñada para ayudar a estudiantes de botánica a aprender nombres científicos y comunes de plantas de forma interactiva y divertida.

### ✨ Características
- 🎮 **Múltiples modos de juego**: Partida rápida, todas las plantas, últimas añadidas
- 🖼️ **Reconocimiento visual**: Identifica plantas por imagen
- 📝 **Gestión completa**: Añadir, editar y eliminar plantas
- 🎯 **Educativo**: Perfecto para aulas y estudio personal
- 💾 **Datos locales**: Sin conexión a internet requerida

## 🔒 Seguridad y Confianza

### ⚠️ Sobre alertas de antivirus
Este ejecutable puede generar **falsos positivos** en Windows Defender. Esto es **completamente normal** en aplicaciones Python compiladas con PyInstaller.

**¿Por qué pasa esto?**
- Las aplicaciones Python compiladas no tienen certificado digital (esta carísimo hermano xd)
- Es un comportamiento estándar de Windows con software nuevo
- **El código fuente está completamente visible** en este repositorio

### ✅ Verificación de seguridad
- **Código 100% opensource**: Todo el código está visible aquí
- **Sin conexiones externas**: No envía datos a ningún servidor
- **Hash SHA256**: Cada release incluye hash para verificación
- **Propósito educativo**: Desarrollado para uso en centros educativos

## 🚀 Instalación y Uso

### Para Estudiantes
1. Descarga el archivo `JuegoPlantas.zip` desde la sección **Releases** de GitHub
2. Descomprime en cualquier carpeta
3. Ejecuta `flora.exe`
4. Si Windows pregunta: **"Más información" → "Ejecutar de todas formas"**

### Para Profesores
1. Descarga y prueba primero en tu equipo
2. Distribuye el ZIP a estudiantes
3. Explica que es normal la alerta de Windows (falso positivo)
4. Lee `README.txt` (en catalán) incluido en el paquete
5. Disponible documentación completa en `INSTRUCCIONES_PRIMERA_VEZ.txt`

## 🛠️ Para Desarrolladores

### Requisitos
- Python 3.9+
- tkinter (incluido en Python)
- Pillow para imágenes

### Ejecutar desde código
```bash
git clone https://github.com/tu-usuario/flora-game.git
cd flora-game
pip install -r requirements.txt
python main.py
```

### Compilar ejecutable
```bash
# Opción 1: Script automático (al escritorio) - RECOMENDADO
generar_exe.bat

# Opción 2: Manual con PyInstaller
pip install pyinstaller pillow
python crear_icono.py
pyinstaller --onefile --windowed --icon=img.ico --add-data "plantas.json;." main.py
```

## 📁 Estructura del Proyecto

```
Floraa/
├── .git/                            # 📂 Control de versiones Git
├── .gitignore                       # 🚫 Archivos ignorados por Git
├── .idea/                           # 💡 Configuración de PyCharm/IntelliJ
├── src/                             # 📂 Código fuente principal
│   ├── __init__.py                  # 🐍 Inicializador de paquete Python
│   ├── controllers/                 # 🎮 Controladores (lógica de negocio)
│   │   ├── __init__.py             # 🐍 Inicializador del módulo
│   │   ├── app_controller.py        # 🏗️ Controlador principal de la aplicación
│   │   ├── juego_controller.py      # 🎯 Lógica del juego y puntuación
│   │   ├── anadir_controller.py     # ➕ Gestión para añadir plantas
│   │   └── editar_controller.py     # ✏️ Edición de plantas existentes
│   ├── models/                      # 📊 Modelos de datos
│   │   ├── __init__.py             # 🐍 Inicializador del módulo
│   │   ├── planta.py               # 🌿 Clase Planta (entidad principal)
│   │   └── planta_repository.py    # 💾 Persistencia y gestión de datos
│   ├── views/                       # 🖼️ Interfaces de usuario (tkinter)
│   │   ├── __init__.py             # 🐍 Inicializador del módulo
│   │   ├── pantalla_inicio.py       # 🏠 Pantalla principal del menú
│   │   ├── pantalla_modos.py        # 🎮 Selección de modos de juego
│   │   ├── pantalla_juego.py        # 🎲 Interfaz principal del juego
│   │   ├── pantalla_anadir.py       # ➕ Formulario para añadir plantas
│   │   ├── pantalla_editar.py       # ✏️ Interfaz de edición
│   │   ├── pantalla_resultado.py    # 🏆 Pantalla de resultados y puntuación
│   │   └── components/              # 🧩 Componentes reutilizables
│   │       ├── __init__.py         # 🐍 Inicializador del módulo
│   │       └── rounded_button.py    # 🔘 Botones personalizados con estilo
│   └── utils/                       # 🔧 Utilidades y herramientas
│       ├── __init__.py             # 🐍 Inicializador del módulo
│       └── file_manager.py         # 📁 Gestión de archivos e imágenes
├── main.py                          # 🚀 Archivo principal de ejecución
├── plantas.json                     # 🌱 Base de datos de plantas (JSON)
├── img.png                          # 🎨 Icono original (formato PNG)
├── img.ico                          # 🔗 Icono convertido (para ejecutable)
├── crear_icono.py                   # 🔄 Script para convertir PNG a ICO
├── generar_exe.bat                  # ⚙️ Script de compilación automática
├── version_info.txt                 # 📋 Metadatos del ejecutable Windows
├── requirements.txt                 # 📦 Dependencias de Python
├── INSTRUCCIONES_PRIMERA_VEZ.txt    # 📖 Guía para usuarios finales
├── SOLUCIONES_ANTIVIRUS.md          # 🛡️ Soluciones para alertas de seguridad
├── COMO_GENERAR_EXE.md              # 🔧 Documentación para desarrolladores
├── LICENSE                          # ⚖️ Licencia MIT del proyecto
├── releases/                        # 📦 Documentación de versiones
│   └── README.md                    # 📚 Información sobre releases
├── README_CA.md                     # 📖 Documentación en catalán
└── README.md                        # 📖 Este archivo de documentación

Archivos generados:
└── ~/Desktop/FloraGame.zip          # 📦 Paquete final (generado en el escritorio)
```

## 🎓 Uso Educativo

### Casos de uso
- **Botánica básica**: Aprender nombres comunes y científicos
- **Biología secundaria**: Reconocimiento visual de especies
- **Universidad**: Práticas de taxonomía vegetal
- **Autoestudio**: Preparación de exámenes

### Ventajas pedagógicas
- **Interactivo**: Más engaging que libros tradicionales
- **Personalizable**: Cada alumno puede añadir sus plantas
- **Sin distracciones**: No requiere internet
- **Multiplataforma**: Funciona en cualquier PC Windows

## 🤝 Contribuir

¡Las contribuciones son bienvenidas!

### Cómo contribuir
1. Fork del repositorio
2. Crea una rama feature (`git checkout -b nueva-caracteristica`)
3. Commit changes (`git commit -am 'Añadir nueva característica'`)
4. Push to branch (`git push origin nueva-caracteristica`)
5. Crear Pull Request

### Ideas de mejoras
- [ ] Modo multijugador local
- [ ] Exportar/importar conjuntos de plantas
- [ ] Estadísticas de progreso
- [ ] Soporte para otros idiomas
- [ ] Versión web

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver archivo [LICENSE](LICENSE) para detalles.

## 👨‍💻 Autor

**Alejandro Expósito Navarro**
- 💻 Desarrollado con la asistencia de GitHub Copilot
- 💝 Dedicado especialmente para Yudi <3
- 🎓 Creado para uso educativo y aprendizaje de botánica
- 🌟 Proyecto opensource sin fines lucrativos
- 📧 Disponible para colaboraciones educativas

## 🙋‍♀️ Soporte

### Para problemas técnicos
- Abre un Issue en GitHub
- Incluye capturas de pantalla si es posible
- Menciona tu versión de Windows

### Para uso educativo
- Contacta directamente para soporte en centros educativos
- Disponible para presentaciones y formación

---

⭐ **Si te gusta el proyecto, ¡dale una estrella!** Ayuda a otros a encontrarlo y aumenta la confianza en la aplicación.
