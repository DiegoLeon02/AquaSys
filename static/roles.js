// Cargar roles al iniciar la página
document.addEventListener('DOMContentLoaded', cargarRoles);

function cargarRoles() {
    fetch('/listar_roles')
        .then(response => response.json())
        .then(data => {
            const rolesList = document.getElementById('rolesList');
            rolesList.innerHTML = ''; 
            data.roles.forEach(role => {
                const li = document.createElement('li');
                li.textContent = `${role.nombre}: ${role.permisos.join(', ')}`;
                rolesList.appendChild(li);
            });
        })
        .catch(error => console.error('Error al cargar roles:', error));
}


document.getElementById('crearRolForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const nombreRol = document.getElementById('nuevoRol').value;
    const permisos = document.getElementById('permisos').value.split(',').map(p => p.trim());

    fetch('/crear_rol', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nombre: nombreRol, permisos })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('mensajeCreacion').textContent = data.message;
        cargarRoles(); 
    })
    .catch(error => {
        document.getElementById('mensajeCreacion').textContent = 'Error al crear rol.';
        console.error('Error:', error);
    });
});


document.getElementById('eliminarRolForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const rolAEliminar = document.getElementById('rolAEliminar').value;

    fetch('/eliminar_rol', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ nombre: rolAEliminar })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('mensajeEliminacion').textContent = data.message;
        cargarRoles(); 
    })
    .catch(error => {
        document.getElementById('mensajeEliminacion').textContent = 'Error al eliminar el rol';
        console.error('Error:', error);
    });
});
