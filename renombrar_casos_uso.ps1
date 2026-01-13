# Script para renombrar archivos de casos de uso
$cuDir = "D:\Proyectos\CDT-Analysis\cu"

$renombres = @{
    "CU-01.tex" = "CU01-CrearMascota.tex"
    "CU-02.tex" = "CU02-EliminarMascota.tex"
    "CU-03.tex" = "CU03-ConsultarMisMascotas.tex"
    "CU-04.tex" = "CU04-ConsultarDetalleMascota.tex"
    "CU-05.tex" = "CU05-AgregarVacuna.tex"
    "CU-07.tex" = "CU07-AgregarAlergia.tex"
    "CU-09.tex" = "CU09-EliminarAlergia.tex"
    "CU-10.tex" = "CU10-AgregarDesparasitacion.tex"
    "CU-11.tex" = "CU11-EliminarDesparasitacion.tex"
    "CU-12.tex" = "CU12-AgregarDocumento.tex"
    "CU-13.tex" = "CU13-EliminarDocumento.tex"
    "CU-14.tex" = "CU14-ConsultarDetalleMascota.tex"
    "CU-14 (1).tex" = "CU14-Duplicado.tex"
    "CU-15.tex" = "CU15-CrearReservacion.tex"
    "CU-16.tex" = "CU16-ConsultarReservaciones.tex"
    "CU-17.tex" = "CU17-EliminarReservacion.tex"
    "CU-18.tex" = "CU18-AgregarServicioReservacion.tex"
    "CU-19.tex" = "CU19-EliminarServicioReservacion.tex"
    "CU-20.tex" = "CU20-PagarReservacion.tex"
    "CU-21.tex" = "CU21-VerDetallesReservacion.tex"
    "CU-22.tex" = "CU22-VerEmpleados.tex"
    "CU-23.tex" = "CU23-AgregarEmpleado.tex"
    "CU-24.tex" = "CU24-EditarEmpleado.tex"
    "CU-25.tex" = "CU25-EliminarEmpleado.tex"
    "CU-27.tex" = "CU27-VerDetalleEmpleado.tex"
    "CU-31.tex" = "CU31-VerCitasEmpleado.tex"
}

$renombrados = 0

foreach ($viejo in $renombres.Keys) {
    $rutaVieja = Join-Path $cuDir $viejo
    $rutaNueva = Join-Path $cuDir $renombres[$viejo]
    
    if (Test-Path $rutaVieja) {
        Rename-Item -Path $rutaVieja -NewName $renombres[$viejo]
        Write-Host "Renombrado: $viejo a $($renombres[$viejo])"
        $renombrados++
    } else {
        Write-Host "No encontrado: $viejo"
    }
}

Write-Host ""
Write-Host "Total renombrados: $renombrados"
