import os
import glob
import random
import re

# Lista de nombres
nombres = [
    "Beltran Saucedo Axel Alejandro",
    "Castillo Aldaba Jared",
    "Ugalde Tellez Aaron",
    "Vazquez Villagran Jorge"
]

# Directorio de casos de uso
cu_dir = r"D:\Proyectos\CDT-Analysis\cu"
archivos = glob.glob(os.path.join(cu_dir, "CU*.tex"))

print(f"Encontrados {len(archivos)} archivos de casos de uso\n")

# Función para procesar cada archivo
def actualizar_caso_uso(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Seleccionar dos nombres diferentes aleatoriamente
    autor, supervisor = random.sample(nombres, 2)
    
    # Reemplazar Autor
    contenido = re.sub(
        r'(\\UCitem\{Autor\}\{\\color\{Gray\})([^}]+)(\})',
        r'\g<1>' + autor + r'\g<3>',
        contenido
    )
    
    # Reemplazar Supervisa
    contenido = re.sub(
        r'(\\UCitem\{Supervisa\}\{\\color\{Gray\})([^}]+)(\})',
        r'\g<1>' + supervisor + r'\g<3>',
        contenido
    )
    
    with open(archivo, 'w', encoding='utf-8') as f:
        f.write(contenido)
    
    nombre_archivo = os.path.basename(archivo)
    print(f"{nombre_archivo:35} | Autor: {autor:35} | Supervisor: {supervisor}")
    return nombre_archivo, autor, supervisor

# Procesar todos los archivos (excepto la plantilla)
random.seed()  # Semilla aleatoria basada en tiempo
resultados = []

for archivo in sorted(archivos):
    if 'plantilla' not in archivo.lower():
        resultado = actualizar_caso_uso(archivo)
        resultados.append(resultado)

print(f"\n✅ Se actualizaron {len(resultados)} casos de uso exitosamente")
