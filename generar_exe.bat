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
        --strip ^
        --add-data "plantas.json;." ^
        --icon="img.ico" ^
        --name "flora" ^
        --version-file="version_info.txt" ^
        --distpath flora_dist ^
        main.py
    if %errorlevel% neq 0 goto :error
    echo.
    echo [4/5] Moviendo ejecutable a carpeta flora...
    if not exist "flora" mkdir flora
    if exist "flora_dist\flora.exe" (
        move /Y "flora_dist\flora.exe" "flora\flora.exe"
        rmdir /s /q flora_dist
    ) else (
        echo ERROR: No se genero el ejecutable
        goto :error
    )
    echo.
    echo [5/6] Copiando instrucciones y documentacion...
    if exist "flora\" (
        copy "plantas.json" "flora\" >nul 2>&1
        copy "INSTRUCCIONES_PRIMERA_VEZ.txt" "flora\" >nul 2>&1
        copy "SOLUCIONES_ANTIVIRUS.md" "flora\" >nul 2>&1
        (
            echo ====================================
            echo FLORA - JOC DE PLANTES
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
        ) > "flora\LLEGEIX-ME.txt"
        echo Instrucciones copiadas correctamente

        echo.
        echo [6/6] Creando archivo ZIP para distribucion...
        powershell -command "try { Compress-Archive -Path 'flora\*' -DestinationPath 'JuegoPlantas.zip' -Force; Write-Host '✓ ZIP creado: JuegoPlantas.zip' } catch { Write-Host 'Error al crear ZIP, pero la carpeta flora está lista' }"
    )
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
        --strip ^
        --add-data "plantas.json;." ^
        --icon="img.ico" ^
        --name "flora" ^
        --version-file="version_info.txt" ^
        --distpath flora_dist ^
        main.py
    if %errorlevel% neq 0 goto :error
    echo.
    echo [4/5] Moviendo ejecutable a carpeta flora...
    if not exist "flora" mkdir flora
    if exist "flora_dist\flora.exe" (
        move /Y "flora_dist\flora.exe" "flora\flora.exe"
        rmdir /s /q flora_dist
    ) else (
        echo ERROR: No se genero el ejecutable
        goto :error
    )
    echo.
    echo [5/6] Copiando instrucciones y documentacion...
    if exist "flora\" (
        copy "plantas.json" "flora\" >nul 2>&1
        copy "INSTRUCCIONES_PRIMERA_VEZ.txt" "flora\" >nul 2>&1
        copy "SOLUCIONES_ANTIVIRUS.md" "flora\" >nul 2>&1
        (
            echo ====================================
            echo FLORA - JOC DE PLANTES
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
        ) > "flora\LLEGEIX-ME.txt"
        echo Instrucciones copiadas correctamente

        echo.
        echo [6/6] Creando archivo ZIP para distribucion...
        powershell -command "try { Compress-Archive -Path 'flora\*' -DestinationPath 'JuegoPlantas.zip' -Force; Write-Host '✓ ZIP creado: JuegoPlantas.zip' } catch { Write-Host 'Error al crear ZIP, pero la carpeta flora está lista' }"
    )
    goto :success
)

REM Si no se encuentra Python
echo No se encontro Python instalado.
echo Descarga e instala Python desde: https://www.python.org/downloads/
echo Asegurate de marcar "Add Python to PATH" durante la instalacion.
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
echo Ubicacion: flora\flora.exe
echo.
echo Contenido del paquete:
echo - flora.exe (programa principal con icono personalizado)
echo - plantas.json (base de datos de plantas)
echo - INSTRUCCIONES_PRIMERA_VEZ.txt
echo - LLEGEIX-ME.txt
echo - SOLUCIONES_ANTIVIRUS.md
echo - JuegoPlantas.zip (paquete completo para distribuir)
echo.
echo IMPORTANTE - Alertas de Antivirus:
echo - El ejecutable NO esta firmado digitalmente (certificado cuesta 300 EUR/ano)
echo - Windows Defender puede mostrar una alerta (ES NORMAL)
echo - Lee SOLUCIONES_ANTIVIRUS.md para mas informacion
echo.
echo Para distribuir:
echo 1. FACIL: Comparte el archivo JuegoPlantas.zip (contiene todo)
echo 2. ALTERNATIVA: Copia la carpeta completa "flora\" a un pendrive
echo 3. En el PC destino: Lee INSTRUCCIONES_PRIMERA_VEZ.txt
echo 4. Primera ejecucion: "Mas informacion" -^> "Ejecutar de todas formas"
echo.
pause

:end
