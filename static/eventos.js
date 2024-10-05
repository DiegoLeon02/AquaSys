document.getElementById('crearEventoForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const nombre = document.getElementById('nombre').value;
    const fecha = document.getElementById('fecha').value;
    const lugar = document.getElementById('lugar').value;
    const descripcion = document.getElementById('descripcion').value;

    
    if (nombre === '' || fecha === '' || lugar === '' || descripcion === '') {
        document.getElementById('mensaje').textContent = 'Formulario incompleto. Por favor, complete todos los campos.';
        return;
    }

   
    fetch('/crear_evento', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nombre, fecha, lugar, descripcion })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('mensaje').textContent = data.message;
    })
    .catch(error => {
        document.getElementById('mensaje').textContent = 'No se pudo conectar con el servidor';
        console.error('Error:', error);
    });
});
