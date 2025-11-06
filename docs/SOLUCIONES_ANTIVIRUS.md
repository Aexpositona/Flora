# Soluciones para Alertas de Antivirus

## ¿Por qué aparece la alerta?

Los ejecutables generados con PyInstaller (Python) son detectados como "sospechosos" por algunos antivirus porque:

1. **No tienen certificado digital** - Los certificados cuestan 300-400€ al año
2. **Son poco comunes** - Pocos programas educativos se distribuyen así
3. **Falsos positivos** - Los antivirus son muy sensivos con ejecutables nuevos

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
Mensaje: "Archivo bloqueado"
Solución:
1. Abrir Avast
2. Ir a "Protección" > "Análisis antivirus"
3. "Excepciones" > "Agregar excepción"
4. Seleccionar flora.exe
```

### Norton
```
Mensaje: "Archivo sospechoso eliminado"
Solución:
1. Abrir Norton
2. "Seguridad del dispositivo" > "Historial"
3. Buscar "flora.exe" > "Restaurar"
4. "Configuración" > "Exclusiones" > Agregar flora.exe
```

### Kaspersky
```
Mensaje: "Aplicación potencialmente no deseada"
Solución:
1. Abrir Kaspersky
2. "Configuración" > "Amenazas y exclusiones"
3. "Exclusiones" > "Agregar"
4. Seleccionar flora.exe
```

## Verificación de Seguridad

El archivo flora.exe es 100% seguro. Puedes verificarlo:

1. **VirusTotal**: Sube el archivo a virustotal.com
2. **Código fuente**: Disponible en el repositorio GitHub
3. **Sin conexión**: El juego no usa internet

## ¿Seguir teniendo problemas?

Si tu antivirus sigue bloqueando el programa:

1. **Desactiva temporalmente** el antivirus
2. **Ejecuta** flora.exe 
3. **Reactiva** el antivirus
4. **Añade excepción** para flora.exe

## Contacto

Para más ayuda, contacta al desarrollador:
- GitHub: Aexpositona
- Email: [tu email si quieres]

**¡El programa es educativo y completamente seguro!**
