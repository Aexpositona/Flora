@echo off
echo Buscando Python en el sistema...

REM Buscar Python en ubicaciones comunes
set PYTHON_EXE=
if exist "C:\Python39\python.exe" set PYTHON_EXE=C:\Python39\python.exe
if exist "C:\Python310\python.exe" set PYTHON_EXE=C:\Python310\python.exe
if exist "C:\Python311\python.exe" set PYTHON_EXE=C:\Python311\python.exe
if exist "C:\Python312\python.exe" set PYTHON_EXE=C:\Python312\python.exe
if exist "%LOCALAPPDATA%\Programs\Python\Python39\python.exe" set PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python39\python.exe
if exist "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" set PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python310\python.exe
if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" set PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python311\python.exe
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" set PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python312\python.exe

REM Intentar usar py.exe (launcher de Python)
py --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Usando py.exe launcher
    echo.
    echo [1/5] Instalando dependencias necesarias...
    py -m pip install pillow pyinstaller
    echo.
    echo [2/5] Creando icono desde img.png...
    py crear_icono.py
    echo.
    echo [3/5] Generando ejecutable optimizado...
    echo (Con metadatos para reducir alertas de antivirus)
    py -m PyInstaller ^
        --onefile ^
        --windowed ^
        --clean ^
        --noconfirm ^
        --optimize=2 ^
        --add-data "plantas.json;." ^
        --icon="img.ico" ^
        --name "flora" ^
        --version-file="version_info.txt" ^
        --distpath flora_dist ^
        main.py
    if %errorlevel% neq 0 goto :error
    echo.
    echo [4/6] Preparando carpeta del juego...
    if not exist "LUDUS HERBARUM" mkdir "LUDUS HERBARUM"
    if exist "flora_dist\flora.exe" (
        move /Y "flora_dist\flora.exe" "LUDUS HERBARUM\flora.exe"
    ) else (
        echo ERROR: No se genero el ejecutable
        goto :error
    )
    echo.
    echo [5/6] Copiando archivos necesarios...
    copy "plantas.json" "LUDUS HERBARUM\" >nul 2>&1
    copy "INSTRUCCIONES_PRIMERA_VEZ.txt" "LUDUS HERBARUM\" >nul 2>&1
    copy "SOLUCIONES_ANTIVIRUS.md" "LUDUS HERBARUM\" >nul 2>&1
    (
        echo ====================================
        echo LUDUS HERBARUM - JOC DE PLANTES
        echo Alejandro Exposito Navarro
        echo ====================================
        echo.
        echo 1. Llegeix INSTRUCCIONS_PRIMERA_VEZ.txt
        echo 2. Executa flora.exe
        echo 3. Gaudeix del joc!
        echo.
        echo Lee INSTRUCCIONS_PRIMERA_VEZ.txt
        echo antes de ejecutar por primera vez
        echo ====================================
    ) > "LUDUS HERBARUM\LLEGEIX-ME.txt"
    echo Archivos copiados correctamente
    echo.
    echo [6/6] Creando archivo ZIP en el escritorio...
    powershell -command "try { Compress-Archive -Path 'LUDUS HERBARUM' -DestinationPath '%USERPROFILE%\Desktop\LUDUS HERBARUM.zip' -Force; Write-Host '✓ ZIP creado en el escritorio: LUDUS HERBARUM.zip' } catch { Write-Host 'Error al crear ZIP en el escritorio' }"
    echo.
    echo Limpiando archivos temporales...
    rmdir /s /q "LUDUS HERBARUM" >nul 2>&1
    rmdir /s /q flora_dist >nul 2>&1
    rmdir /s /q build >nul 2>&1
    rmdir /s /q __pycache__ >nul 2>&1
    del flora.spec >nul 2>&1
    echo Limpieza completada
    goto :success
)

REM Si encontramos Python directamente
if not "%PYTHON_EXE%"=="" (
    echo Encontrado Python en: %PYTHON_EXE%
    echo.
    echo [1/5] Instalando dependencias necesarias...
    "%PYTHON_EXE%" -m pip install pillow pyinstaller
    echo.
    echo [2/5] Creando icono desde img.png...
    "%PYTHON_EXE%" crear_icono.py
    echo.
    echo [3/5] Generando ejecutable optimizado...
    echo (Con metadatos para reducir alertas de antivirus)
    "%PYTHON_EXE%" -m PyInstaller ^
        --onefile ^
        --windowed ^
        --clean ^
        --noconfirm ^
        --optimize=2 ^
        --add-data "plantas.json;." ^
        --icon="img.ico" ^
        --name "flora" ^
        --version-file="version_info.txt" ^
        --distpath flora_dist ^
        main.py
    if %errorlevel% neq 0 goto :error
    echo.
    echo [4/6] Preparando carpeta del juego...
    if not exist "LUDUS HERBARUM" mkdir "LUDUS HERBARUM"
    if exist "flora_dist\flora.exe" (
        move /Y "flora_dist\flora.exe" "LUDUS HERBARUM\flora.exe"
    ) else (
        echo ERROR: No se genero el ejecutable
        goto :error
    )
    echo.
    echo [5/6] Copiando archivos necesarios...
    copy "plantas.json" "LUDUS HERBARUM\" >nul 2>&1
    copy "INSTRUCCIONES_PRIMERA_VEZ.txt" "LUDUS HERBARUM\" >nul 2>&1
    copy "SOLUCIONES_ANTIVIRUS.md" "LUDUS HERBARUM\" >nul 2>&1
    (
        echo ====================================
        echo LUDUS HERBARUM - JOC DE PLANTES
        echo Alejandro Exposito Navarro
        echo ====================================
        echo.
        echo 1. Llegeix INSTRUCCIONS_PRIMERA_VEZ.txt
        echo 2. Executa flora.exe
        echo 3. Gaudeix del joc!
        echo.
        echo Lee INSTRUCCIONS_PRIMERA_VEZ.txt
        echo antes de ejecutar por primera vez
        echo ====================================
    ) > "LUDUS HERBARUM\LLEGEIX-ME.txt"
    echo Archivos copiados correctamente
    echo.
    echo [6/6] Creando archivo ZIP en el escritorio...
    powershell -command "try { Compress-Archive -Path 'LUDUS HERBARUM' -DestinationPath '%USERPROFILE%\Desktop\LUDUS HERBARUM.zip' -Force; Write-Host '✓ ZIP creado en el escritorio: LUDUS HERBARUM.zip' } catch { Write-Host 'Error al crear ZIP en el escritorio' }"
    echo.
    echo Limpiando archivos temporales...
    rmdir /s /q "LUDUS HERBARUM" >nul 2>&1
    rmdir /s /q flora_dist >nul 2>&1
    rmdir /s /q build >nul 2>&1
    rmdir /s /q __pycache__ >nul 2>&1
    del flora.spec >nul 2>&1
    echo Limpieza completada
    goto :success
)

REM Si no se encuentra Python
echo No se encontro Python instalado.
echo Descarga e instala Python desde: https://www.python.org/downloads/
echo Asegurate de marcar "Add Python to PATH" durante la instalación.
pause
goto :end

:error
echo.
echo ====================================
echo ERROR al generar el ejecutable
echo ====================================
echo.
echo Verifica:
echo 1. Python esta instalado correctamente
echo 2. Las dependencias se instalaron (pillow, pyinstaller)
echo 3. El archivo main.py existe
echo 4. La carpeta src/ tiene todos los archivos
echo 5. El archivo img.png existe
echo.
pause
goto :end

:success
echo.
echo ====================================
echo Ejecutable generado exitosamente!
echo ====================================
echo.
echo Archivo generado: LUDUS HERBARUM.zip (en el Escritorio)
echo.
echo Contenido del ZIP:
echo LUDUS HERBARUM/
echo   ├─ flora.exe (programa principal con icono personalizado)
echo   ├─ plantas.json (base de datos de plantas)
echo   ├─ INSTRUCCIONES_PRIMERA_VEZ.txt
echo   ├─ LLEGEIX-ME.txt
echo   └─ SOLUCIONES_ANTIVIRUS.md
echo.
echo IMPORTANTE - Alertas de Antivirus:
echo - El ejecutable NO esta firmado digitalmente (está carísimo hermano xd)
echo - Windows Defender puede mostrar una alerta (ES NORMAL)
echo - Lee SOLUCIONES_ANTIVIRUS.md para mas información
echo.
echo Para distribuir:
echo 1. Comparte el archivo LUDUS HERBARUM.zip desde tu Escritorio
echo 2. En el PC destino: Extrae el ZIP y lee INSTRUCCIONES_PRIMERA_VEZ.txt
echo 3. Primera ejecución: "Mas información" -^> "Ejecutar de todas formas"
echo.
pause

:end
