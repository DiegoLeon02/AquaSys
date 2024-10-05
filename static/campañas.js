document.addEventListener('DOMContentLoaded', () => {
    const formCampaña = document.getElementById('formCampaña');
    const mensajeDiv = document.getElementById('mensaje');
    const campañasBody = document.getElementById('campañasBody');

    formCampaña.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const nombre = document.getElementById('nombre').value;
        const objetivo = document.getElementById('objetivo').value;
        const fechaInicio = document.getElementById('fechaInicio').value;
        const fechaFin = document.getElementById('fechaFin').value;
        const texto = document.getElementById('texto').value;
        const multimedia = document.getElementById('multimedia').files[0];

        if (!nombre || !objetivo || !fechaInicio || !fechaFin || !texto || !multimedia) {
            mensajeDiv.innerHTML = "Campo obligatorio";
            return;
        }

       
        const formData = new FormData();
        formData.append('nombre', nombre);
        formData.append('objetivo', objetivo);
        formData.append('fechaInicio', fechaInicio);
        formData.append('fechaFin', fechaFin);
        formData.append('texto', texto);
        formData.append('multimedia', multimedia);

        try {
            const response = await fetch('/crear_campaña', {
                method: 'POST',
                body: formData
            });
            const result = await response.json();
            if (result.success) {
                mensajeDiv.innerHTML = "Campaña creada exitosamente";
                
                const row = document.createElement('tr');
                row.innerHTML = `<td>${nombre}</td><td>${objetivo}</td><td><button onclick="eliminarCampaña('${nombre}')">Eliminar</button></td>`;
                campañasBody.appendChild(row);
            } else {
                mensajeDiv.innerHTML = result.message || "Error al crear la campaña";
            }
        } catch (error) {
            mensajeDiv.innerHTML = "Hubo un problema al crear la campaña, inténtelo más tarde";
        }
    });
});

async function eliminarCampaña(nombre) {
    const response = await fetch(`/eliminar_campaña/${nombre}`, {
        method: 'DELETE'
    });
    const result = await response.json();
    if (result.success) {
        document.getElementById('mensaje').innerHTML = "Campaña eliminada";
       
        location.reload(); 
    } else {
        document.getElementById('mensaje').innerHTML = "¡No se pudo eliminar la campaña!";
    }
}
