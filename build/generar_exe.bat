@echo off
echo ====================================
echo LUDUS HERBARUM - BUILD SCRIPT
echo ====================================
echo.

REM Cambiar al directorio raíz del proyecto
cd /d "%~dp0.."

REM Buscar Python en ubicaciones comunes
set PYTHON_EXE=
if exist "C:\Python39\python.exe" set PYTHON_EXE=C:\Python39\python.exe
if exist "C:\Python310\python.exe" set PYTHON_EXE=C:\Python310\python.exe
if exist "C:\Python311\python.exe" set PYTHON_EXE=C:\Python311\python.exe
if exist "C:\Python312\python.exe" set PYTHON_EXE=C:\Python312\python.exe
if exist "C:\Python313\python.exe" set PYTHON_EXE=C:\Python313\python.exe
if exist "%LOCALAPPDATA%\Programs\Python\Python39\python.exe" set PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python39\python.exe
if exist "%LOCALAPPDATA%\Programs\Python\Python310\python.exe" set PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python310\python.exe
if exist "%LOCALAPPDATA%\Programs\Python\Python311\python.exe" set PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python311\python.exe
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" set PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python312\python.exe
if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" set PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python313\python.exe

REM Intentar usar py.exe (launcher de Python)
py --version >nul 2>&1
if %errorlevel% equ 0 (
    echo [1/6] Instalando dependencias...
    py -m pip install -r requirements.txt
    py -m pip install pyinstaller
    echo.

    echo [2/6] Copiando imagen a assets...
    if exist "img.png" (
        copy "img.png" "assets\images\" >nul 2>&1
        echo Imagen copiada a assets/images/
    )

    echo [3/6] Creando icono...
    py build\crear_icono.py
    echo.

    echo [4/6] Compilando ejecutable...
    py -m PyInstaller --onefile --windowed --clean --noconfirm --optimize=2 --add-data "assets/data/plantas.json;assets/data/" --icon="assets/icons/img.ico" --name "flora" --version-file="build/version_info.txt" --distpath "dist/temp" main.py
    if %errorlevel% neq 0 goto :error
    echo.

    echo [5/6] Preparando distribución...
    if not exist "dist\LUDUS HERBARUM" mkdir "dist\LUDUS HERBARUM"
    if exist "dist\temp\flora.exe" (
        copy "dist\temp\flora.exe" "dist\LUDUS HE
        RBARUM\" >nul
        copy "assets\data\plantas.json" "dist\LUDUS HERBARUM\" >nul
        copy "docs\INSTRUCCIONES_PRIMERA_VEZ.txt" "dist\LUDUS HERBARUM\" >nul
        copy "docs\SOLUCIONES_ANTIVIRUS.md" "dist\LUDUS HERBARUM\" >nul
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
        ) > "dist\LUDUS HERBARUM\LLEGEIX-ME.txt"
        echo Archivos copiados correctamente
    ) else (
        echo ERROR: No se encontró el ejecutable
        goto :error
    )
    echo.

    echo [6/6] Creando ZIP en el escritorio...
    powershell -command "try { Compress-Archive -Path 'dist\LUDUS HERBARUM' -DestinationPath '%USERPROFILE%\Desktop\LUDUS HERBARUM.zip' -Force; Write-Host '✓ ZIP creado: LUDUS HERBARUM.zip' } catch { Write-Host 'Error al crear ZIP' }"
    echo.

    echo Limpiando archivos temporales...
    rmdir /s /q "dist\LUDUS HERBARUM" >nul 2>&1
    rmdir /s /q "dist\temp" >nul 2>&1
    rmdir /s /q "build\build" >nul 2>&1
    rmdir /s /q "__pycache__" >nul 2>&1
    del "flora.spec" >nul 2>&1
    echo Limpieza completada

    goto :success
)

REM Si encontramos Python directamente
if not "%PYTHON_EXE%"=="" (
    echo [1/6] Instalando dependencias...
    "%PYTHON_EXE%" -m pip install -r requirements.txt
    "%PYTHON_EXE%" -m pip install pyinstaller
    echo.

    echo [2/6] Copiando imagen a assets...
    if exist "img.png" (
        copy "img.png" "assets\images\" >nul 2>&1
        echo Imagen copiada a assets/images/
    )

    echo [3/6] Creando icono...
    "%PYTHON_EXE%" build\crear_icono.py
    echo.

    echo [4/6] Compilando ejecutable...
    "%PYTHON_EXE%" -m PyInstaller --onefile --windowed --clean --noconfirm --optimize=2 --add-data "assets/data/plantas.json;assets/data/" --icon="assets/icons/img.ico" --name "flora" --version-file="build/version_info.txt" --distpath "dist/temp" main.py
    if %errorlevel% neq 0 goto :error
    echo.

    echo [5/6] Preparando distribución...
    if not exist "dist\LUDUS HERBARUM" mkdir "dist\LUDUS HERBARUM"
    if exist "dist\temp\flora.exe" (
        copy "dist\temp\flora.exe" "dist\LUDUS HERBARUM\" >nul
        copy "assets\data\plantas.json" "dist\LUDUS HERBARUM\" >nul
        copy "docs\INSTRUCCIONES_PRIMERA_VEZ.txt" "dist\LUDUS HERBARUM\" >nul
        copy "docs\SOLUCIONES_ANTIVIRUS.md" "dist\LUDUS HERBARUM\" >nul
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
        ) > "dist\LUDUS HERBARUM\LLEGEIX-ME.txt"
        echo Archivos copiados correctamente
    ) else (
        echo ERROR: No se encontró el ejecutable
        goto :error
    )
    echo.

    echo [6/6] Creando ZIP en el escritorio...
    powershell -command "try { Compress-Archive -Path 'dist\LUDUS HERBARUM' -DestinationPath '%USERPROFILE%\Desktop\LUDUS HERBARUM.zip' -Force; Write-Host '✓ ZIP creado: LUDUS HERBARUM.zip' } catch { Write-Host 'Error al crear ZIP' }"
    echo.

    echo Limpiando archivos temporales...
    rmdir /s /q "dist\LUDUS HERBARUM" >nul 2>&1
    rmdir /s /q "dist\temp" >nul 2>&1
    rmdir /s /q "build\build" >nul 2>&1
    rmdir /s /q "__pycache__" >nul 2>&1
    del "flora.spec" >nul 2>&1
    echo Limpieza completada

    goto :success
)

REM Si no se encuentra Python
echo No se encontró Python instalado.
echo Descarga e instala Python desde: https://www.python.org/downloads/
echo Asegúrate de marcar "Add Python to PATH" durante la instalación.
pause
goto :end

:error
echo.
echo ====================================
echo ERROR al generar el ejecutable
echo ====================================
echo.
echo Verifica:
echo 1. Python está instalado correctamente
echo 2. Existe el archivo main.py
echo 3. Existe assets/images/img.png
echo 4. Las dependencias se instalaron correctamente
echo.
pause
goto :end

:success
echo.
echo ====================================
echo ¡BUILD COMPLETADO EXITOSAMENTE!
echo ====================================
echo.
echo Archivo generado: LUDUS HERBARUM.zip (en el Escritorio)
echo.
echo Contenido del ZIP:
echo LUDUS HERBARUM/
echo   ├─ flora.exe
echo   ├─ plantas.json
echo   ├─ INSTRUCCIONES_PRIMERA_VEZ.txt
echo   ├─ LLEGEIX-ME.txt
echo   └─ SOLUCIONES_ANTIVIRUS.md
echo.
echo Para distribuir:
echo 1. Comparte LUDUS HERBARUM.zip desde tu Escritorio
echo 2. Los estudiantes extraen y siguen las instrucciones
echo 3. ¡Listo para usar!
echo.
pause

:end
