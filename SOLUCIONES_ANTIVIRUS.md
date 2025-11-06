# Soluciones para Alertas de Antivirus

## ¿Por qué aparece la alerta?

Los ejecutables generados con PyInstaller (Python) son detectados como "sospechosos" por algunos antivirus porque:

1. **No tienen certificado digital** - Los certificados cuestan 300-400€ al año
2. **Son poco comunes** - Pocos programas educativos se distribuyen así
3. **Falsos positivos** - Los antivirus son muy sensibles con ejecutables nuevos

## Soluciones por Antivirus

### Windows Defender
```
Mensaje: "Windows protegió tu PC"
Solución:
1. Clic en "Más información"
2. Clic en "Ejecutar de todas formas"
```

### Avast / AVG
```
Mensaje: "Archivo sospechoso bloqueado"
Solución:
1. Abrir Avast
2. Ir a "Protección" > "Escudo de archivos"
3. Agregar excepción para la carpeta del juego
```

### Norton / Symantec
```
Mensaje: "Archivo de riesgo eliminado"
Solución:
1. Abrir Norton Security
2. Ir a "Configuración" > "Antivirus" > "Exclusiones"
3. Agregar la carpeta del juego
```

### McAfee
```
Mensaje: "Amenaza bloqueada"
Solución:
1. Abrir McAfee
2. Ir a "Configuración" > "Protección en tiempo real"
3. Agregar exclusión para el archivo flora.exe
```

### Kaspersky
```
Mensaje: "Archivo sospechoso detectado"
Solución:
1. Abrir Kaspersky
2. Ir a "Configuración" > "Exclusiones"
3. Agregar excepción para el archivo
```

## Verificación de Seguridad

Puedes verificar que el archivo es seguro:

1. **VirusTotal**: Sube el archivo a virustotal.com
2. **Código fuente**: Disponible públicamente en GitHub
3. **Sin conexión**: El programa no se conecta a internet
4. **Sin permisos**: No requiere privilegios de administrador

## Para Centros Educativos

Si eres profesor/administrador de IT:

1. **Añade exclusión** en el antivirus corporativo
2. **Carpeta recomendada**: `C:\Juegos Educativos\Flora\`
3. **Documentación**: Muestra este archivo al departamento IT
4. **Alternativa**: Ejecutar desde memoria USB (sin instalar)

## Contacto Técnico

- **Desarrollador**: Alejandro Expósito Navarro
- **Código fuente**: Disponible en repositorio público
- **Licencia**: MIT (código abierto)

---

**Este programa es 100% seguro y está diseñado específicamente para uso educativo.**
