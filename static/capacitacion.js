document.getElementById('asignarCursoForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const empleadoId = document.getElementById('empleados').value;
    const cursoId = document.getElementById('curso').value;

    fetch('/asignar_curso', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ empleadoId, cursoId })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('mensajeAsignacion').textContent = data.message;
    })
    .catch(error => {
        document.getElementById('mensajeAsignacion').textContent = 'Error al conectar con el servidor, intente nuevamente más tarde';
        console.error('Error:', error);
    });
});

document.getElementById('eliminarCursoForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const empleadoId = document.getElementById('empleadoId').value.trim();

    fetch('/eliminar_curso', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ empleadoId })
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
