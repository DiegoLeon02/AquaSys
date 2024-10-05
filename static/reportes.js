document.getElementById('generarReporteForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const parametros = document.getElementById('parametros').value.trim();

   
    if (!parametros) {
        document.getElementById('mensajeGeneracion').textContent = 'Parametros invalidos';
        return;
    }

    fetch('/generar_reporte', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ parametros })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('mensajeGeneracion').textContent = data.message;
    })
    .catch(error => {
        document.getElementById('mensajeGeneracion').textContent = 'No se pudo conectar con el servidor';
        console.error('Error:', error);
    });
});

document.getElementById('eliminarReporteForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const reporteId = document.getElementById('reporteId').value.trim();

    fetch('/eliminar_reporte', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ reporteId })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('mensajeEliminacion').textContent = data.message;
    })
    .catch(error => {
        document.getElementById('mensajeEliminacion').textContent = 'No se pudo conectar con el servidor';
        console.error('Error:', error);
    });
});
