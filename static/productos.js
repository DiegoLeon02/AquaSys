document.getElementById('crearProductoForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const nombre = document.getElementById('nombre').value;
    const descripcion = document.getElementById('descripcion').value;
    const precio = document.getElementById('precio').value;
    const stock = document.getElementById('stock').value;

    fetch('/crear_producto', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nombre, descripcion, precio, stock })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('mensajeCreacion').textContent = data.message;
        if (data.success) {
            document.getElementById('crearProductoForm').reset(); 
        }
    })
    .catch(error => {
        document.getElementById('mensajeCreacion').textContent = 'Error al añadir el producto';
        console.error('Error:', error);
    });
});
