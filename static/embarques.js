document.getElementById('crearEmbarqueForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const destino = document.getElementById('destino').value;
    const fechaSalida = document.getElementById('fechaSalida').value;
    const numeroContenedor = document.getElementById('numeroContenedor').value;
    const detallesCarga = document.getElementById('detallesCarga').value;
    const contactoDestinatario = document.getElementById('contactoDestinatario').value;

    fetch('/crear_embarque', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ destino, fechaSalida, numeroContenedor, detallesCarga, contactoDestinatario })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('mensajeCreacion').textContent = data.message;
        if (data.success) {
            document.getElementById('crearEmbarqueForm').reset(); 
        }
    })
    .catch(error => {
        document.getElementById('mensajeCreacion').textContent = 'Error al crear embarque';
        console.error('Error:', error);
    });
});
