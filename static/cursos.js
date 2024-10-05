document.getElementById('subirCursoForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const nombreCurso = document.getElementById('nombreCurso').value;
    const descripcionCurso = document.getElementById('descripcionCurso').value;
    const pdfCurso = document.getElementById('pdfCurso').files[0];

    
    const formData = new FormData();
    formData.append('nombreCurso', nombreCurso);
    formData.append('descripcionCurso', descripcionCurso);
    formData.append('pdfCurso', pdfCurso);

    fetch('/subir_curso', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('mensajeSubir').textContent = data.message;
       
    })
    .catch(error => {
        document.getElementById('mensajeSubir').textContent = 'No se pudo conectar con el servidor';
        console.error('Error:', error);
    });
});

document.getElementById('editarCursoForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const cursoID = document.getElementById('cursoID').value;
    const nuevoNombreCurso = document.getElementById('nuevoNombreCurso').value;
    const nuevaDescripcionCurso = document.getElementById('nuevaDescripcionCurso').value;
    const nuevoPdfCurso = document.getElementById('nuevoPdfCurso').files[0];

    
    const formData = new FormData();
    formData.append('cursoID', cursoID);
    if (nuevoNombreCurso) formData.append('nuevoNombreCurso', nuevoNombreCurso);
    if (nuevaDescripcionCurso) formData.append('nuevaDescripcionCurso', nuevaDescripcionCurso);
    if (nuevoPdfCurso) formData.append('nuevoPdfCurso', nuevoPdfCurso);

    fetch('/editar_curso', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('mensajeEditar').textContent = data.message;
        
    })
    .catch(error => {
        document.getElementById('mensajeEditar').textContent = 'No se pudo conectar con el servidor';
        console.error('Error:', error);
    });
});

document.getElementById('borrarCursoForm').addEventListener('submit', function(event) {
    event.preventDefault(); 

    const cursoIDEliminar = document.getElementById('cursoIDEliminar').value;

    fetch('/borrar_curso', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ cursoID: cursoIDEliminar })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('mensajeBorrar').textContent = data.message;
        
    })
    .catch(error => {
        document.getElementById('mensajeBorrar').textContent = 'No se pudo conectar con el servidor';
        console.error('Error:', error);
    });
});
