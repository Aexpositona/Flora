# 🌱 LUDUS HERBARUM - Juego Educativo de Plantas

[![Licencia: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Educativo](https://img.shields.io/badge/Tipo-Educativo-green.svg)]()
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)]()

## 📚 Descripción

**LUDUS HERBARUM** es una aplicación educativa opensource diseñada para ayudar a estudiantes de botánica a aprender nombres científicos y comunes de plantas de forma interactiva y divertida.

### ✨ Características

- 🎯 **Modos de juego múltiples** - Aprende de diferentes formas
- 🌿 **Base de datos de plantas** - Nombres científicos y comunes
- 📊 **Sistema de puntuación** - Seguimiento de progreso
- 🎨 **Interfaz intuitiva** - Diseño limpio y amigable
- 💾 **Gestión de datos** - Añadir/editar plantas fácilmente
- 🔄 **Multiplataforma** - Windows, Linux, macOS

## 🚀 Instalación Rápida

### Para Estudiantes (Solo usar)
1. Descarga `LUDUS HERBARUM.zip` desde [Releases](https://github.com/Aexpositona/Flora/releases/latest)
2. Extrae el archivo ZIP
3. Lee `INSTRUCCIONES_PRIMERA_VEZ.txt`
4. Ejecuta `flora.exe`

### Para Desarrolladores
```bash
git clone https://github.com/Aexpositona/Flora.git
cd Flora
pip install -r requirements.txt
python main.py
```

## 📁 Estructura del Proyecto

```
LUDUS-HERBARUM/
├── main.py              # Punto de entrada principal
├── src/                 # Código fuente organizado
│   ├── controllers/     # Lógica de control
│   ├── models/         # Modelos de datos
│   ├── views/          # Interfaz de usuario
│   └── utils/          # Utilidades
├── assets/             # Recursos
│   ├── data/          # Datos del juego
│   ├── images/        # Imágenes
│   └── icons/         # Iconos
├── docs/              # Documentación
├── build/            # Scripts de compilación
└── dist/            # Distribución (temporal)
```

## 🛠️ Desarrollo

### Requisitos
- Python 3.9+
- tkinter (incluido en Python)
- Pillow (para iconos)

### Compilar Ejecutable
```bash
# En Windows
build/generar_exe.bat

# El ZIP se creará en tu Escritorio
```

## 🎮 Cómo Jugar

1. **Añadir plantas** - Gestiona tu base de datos
2. **Elegir modo** - Diferentes tipos de quiz
3. **Jugar** - Responde preguntas sobre plantas
4. **Ver resultados** - Revisa tu puntuación

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver [LICENSE](../LICENSE) para detalles.

## 👨‍💻 Autor

**Alejandro Expósito Navarro**
- GitHub: [@Aexpositona](https://github.com/Aexpositona)

## 🙏 Agradecimientos

- A todos los estudiantes que usan la aplicación
- A la comunidad de Python por las herramientas
- A los proyectos opensource que inspiraron este trabajo

---

*Fet amb 💚 per la Yudi <3*
