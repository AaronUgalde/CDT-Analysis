import os
import random
import re

# Lista de nombres disponibles
nombres = [
    "Beltran Saucedo Axel Alejandro",
    "Castillo Aldaba Jared",
    "Ugalde Tellez Aaron",
    "Vazquez Villagran Jorge"
]

# Directorio de casos de uso
directorio = r"D:\Proyectos\CDT-Analysis\cu"

# Obtener todos los archivos .tex (excluyendo la plantilla)
archivos = [f for f in os.listdir(directorio) 
            if f.startswith("CU") and f.endswith(".tex") and "plantilla" not in f.lower()]

print(f"Encontrados {len(archivos)} archivos de casos de uso")
print("=" * 60)

# Procesar cada archivo
for archivo in sorted(archivos):
    ruta_completa = os.path.join(directorio, archivo)
    
    # Leer el contenido del archivo
    with open(ruta_completa, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Seleccionar aleatoriamente dos nombres diferentes
    nombres_seleccionados = random.sample(nombres, 2)
    autor = nombres_seleccionados[0]
    supervisa = nombres_seleccionados[1]
    
    # Reemplazar Autor
    contenido = re.sub(
        r'(\\UCitem\{Autor\}\{\\color\{Gray\})([^}]+)(\})',
        rf'\1{autor}\3',
        contenido
    )
    
    # Reemplazar Supervisa
    contenido = re.sub(
        r'(\\UCitem\{Supervisa\}\{\\color\{Gray\}\[?)([^\]]+)(\]?\})',
        rf'\1{supervisa}\3',
        contenido
    )
    
    # Guardar el archivo modificado
    with open(ruta_completa, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    print(f"{archivo:30} -> Autor: {autor:35} | Supervisa: {supervisa}")

print("=" * 60)
print("✓ Proceso completado exitosamente")
