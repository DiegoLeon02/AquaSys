document.getElementById('crearPerfilForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const nombre = document.getElementById('nombre').value.trim();
    const apellido = document.getElementById('apellido').value.trim();
    const numero = document.getElementById('numero').value.trim();
    const fechaNacimiento = document.getElementById('fecha_nacimiento').value;
    const cedula = document.getElementById('cedula').value.trim();
    const lugarResidencia = document.getElementById('lugar_residencia').value.trim();
    const correo = document.getElementById('correo').value.trim();

   
    if (!nombre || !apellido || !numero || !cedula) {
        document.getElementById('mensajeCreacion').textContent = 'Campo obligatorio';
        return;
    }

    const perfilEmpleado = {
        nombre,
        apellido,
        numero,
        fechaNacimiento,
        cedula,
        lugarResidencia,
        correo
    };

    fetch('/crear_perfil_empleado', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(perfilEmpleado)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('mensajeCreacion').textContent = data.message;
    })
    .catch(error => {
        document.getElementById('mensajeCreacion').textContent = 'No se pudo conectar con el servidor';
        console.error('Error:', error);
    });
});
