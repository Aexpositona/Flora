# 🌱 LUDUS HERBARUM - Joc Educatiu de Plantes

[![Licència: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Educatiu](https://img.shields.io/badge/Tipus-Educatiu-green.svg)]()
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)]()

## 📚 Descripció

**LUDUS HERBARUM** és una aplicació educativa opensource dissenyada per ajudar a estudiants de botànica a aprendre noms científics i comuns de plantes de forma interactiva i divertida.

### ✨ Característiques
- 🎮 **Múltiples modes de joc**: Partida ràpida, totes les plantes, últimes afegides
- 🖼️ **Reconeixement visual**: Identifica plantes per imatge
- 📝 **Gestió completa**: Afegir, editar i eliminar plantes
- 🎯 **Educatiu**: Perfect per aules i estudi personal
- 💾 **Dades locals**: Sense connexió a internet requerida

## 🔒 Seguretat i Confiança

### ⚠️ Sobre alertes d'antivirus
Aquest executable pot generar **falsos positius** a Windows Defender. Això és **completament normal** en aplicacions Python compilades amb PyInstaller.

**Per què passa això?**
- Les aplicacions Python compilades no tenen certificat digital (està caríssim germà xd)
- És un comportament estàndard de Windows amb programari nou
- **El codi font està completament visible** en aquest repositori

### ✅ Verificació de seguretat
- **Codi 100% opensource**: Tot el codi està visible aquí
- **Sense connexions externes**: No envia dades a cap servidor
- **Hash SHA256**: Cada release inclou hash per verificació
- **Propòsit educatiu**: Desenvolupat per ús en centres educatius

## 🚀 Instal·lació i Ús

### Per Estudiants
1. Descarrega l'arxiu `LUDUS HERBARUM.zip` des de la secció **Releases** de GitHub
2. Descomprimeix en qualsevol carpeta
3. Executa `flora.exe`
4. Si Windows pregunta: **"Més informació" → "Executar de totes maneres"**

### Per Professors
1. Descarrega i prova primer al teu equip
2. Distribueix el ZIP als estudiants
3. Explica que és normal l'alerta de Windows (fals positiu)
4. Llegeix `LLEGEIX-ME.txt` (en català) inclòs al paquet
5. Disponible documentació completa a `INSTRUCCIONS_PRIMERA_VEZ.txt`

## 🛠️ Per Desenvolupadors

### Requisits
- Python 3.9+
- tkinter (inclòs a Python)
- Pillow per imatges

### Executar des del codi
```bash
git clone https://github.com/Aexpositona/Flora.git
cd Flora
pip install -r requirements.txt
python src/main.py
```

### Compilar executable
```bash
# Opció 1: Script automàtic (a l'escriptori) - RECOMANAT
build/generar_exe.bat

# Opció 2: Manual amb PyInstaller
pip install pyinstaller pillow
python build/crear_icono.py
pyinstaller --onefile --windowed --icon=assets/icons/img.ico --add-data "assets/data/plantas.json;." src/main.py
```

## 📁 Estructura del Projecte

```
LUDUS-HERBARUM/
├── src/                    # Codi font
│   ├── main.py            # Punt d'entrada
│   ├── controllers/       # Lògica de control
│   ├── models/           # Models de dades
│   ├── views/            # Interfície d'usuari
│   └── utils/            # Utilitats
├── assets/               # Recursos
│   ├── data/            # Dades del joc
│   ├── images/          # Imatges
│   └── icons/           # Icones
├── docs/                # Documentació
├── build/              # Scripts de compilació
└── dist/              # Distribució
```

## 🎮 Com Jugar

1. **Afegir plantes** - Gestiona la teva base de dades
2. **Triar mode** - Diferents tipus de quiz
3. **Jugar** - Respon preguntes sobre plantes
4. **Veure resultats** - Revisa la teva puntuació

## 🤝 Contribuir

1. Fork el projecte
2. Crea una branca feature (`git checkout -b feature/nova-funcionalitat`)
3. Commit els teus canvis (`git commit -am 'Afegir nova funcionalitat'`)
4. Push a la branca (`git push origin feature/nova-funcionalitat`)
5. Obre un Pull Request

## 📄 Llicència

Aquest projecte està sota la Llicència MIT - veure [LICENSE](LICENSE) per detalls.

## 👨‍💻 Autor

**Alejandro Expósito Navarro**
- GitHub: [@Aexpositona](https://github.com/Aexpositona)

## 🙏 Agraïments

- A tots els estudiants que usen l'aplicació
- A la comunitat de Python per les eines
- Als projectes opensource que van inspirar aquest treball

---

*Fet amb 💚 per la Yudi <3*
python src/main.py
```

### Compilar executable
```bash
# Opció 1: Script automàtic (a l'escriptori) - RECOMANAT
build/generar_exe.bat

# Opció 2: Manual amb PyInstaller
pip install pyinstaller pillow
python build/crear_icono.py
pyinstaller --onefile --windowed --icon=assets/icons/img.ico --add-data "assets/data/plantas.json;." src/main.py
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
