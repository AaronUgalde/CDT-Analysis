# Script para corregir referencias de actores
$cuDir = "D:\Proyectos\CDT-Analysis\cu"

# Obtener todos los archivos .tex
$texFiles = Get-ChildItem -Path $cuDir -Filter "*.tex"

$cambios = @{
    # Cliente es sinónimo de Propietario
    "Actor}{Cliente" = "Actor}{\hyperlink{Propietario}{Propietario}"
    # Recepcionista puede ser manejado por Administrador
    "Recepcionista o Administrador" = "\hyperlink{Administrador}{Administrador}"
    "Cliente o Recepcionista" = "\hyperlink{Propietario}{Propietario} o \hyperlink{Administrador}{Administrador}"
    # Veterinario y Cuidador son tipos de Empleado
    "Recepcionista, Veterinario o Cuidador" = "\hyperlink{Administrador}{Administrador} o \hyperlink{Empleado}{Empleado}"
    "Recepcionista, Administrador o Veterinario" = "\hyperlink{Administrador}{Administrador} o \hyperlink{Empleado}{Empleado}"
    # Usuario autenticado puede ser cualquier actor
    "Actor}{Usuario autenticado" = "Actor}{\hyperlink{Propietario}{Propietario} o \hyperlink{Administrador}{Administrador}"
}

$archivosModificados = 0

foreach ($archivo in $texFiles) {
    $contenido = Get-Content -Path $archivo.FullName -Raw -Encoding UTF8
    $contenidoOriginal = $contenido
    
    foreach ($viejo in $cambios.Keys) {
        if ($contenido -match [regex]::Escape($viejo)) {
            $contenido = $contenido -replace [regex]::Escape($viejo), $cambios[$viejo]
            Write-Host "Corrigiendo en $($archivo.Name): $viejo"
        }
    }
    
    if ($contenido -ne $contenidoOriginal) {
        Set-Content -Path $archivo.FullName -Value $contenido -Encoding UTF8 -NoNewline
        $archivosModificados++
    }
}

Write-Host ""
Write-Host "Total de archivos modificados: $archivosModificados"
