document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); 
    const correo = document.getElementById('correo').value;
    const contrasena = document.getElementById('contrasena').value;

    
    if (correo === '' || contrasena === '') {
        document.getElementById('mensaje').textContent = 'Complete todos los campos solicitados';
        return;
    }

    
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ correo, contrasena })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('mensaje').textContent = data.message;
        if (data.status === 'success') {
            
            window.location.href = '/menu';
        }
    })
    .catch(error => {
        document.getElementById('mensaje').textContent = 'Error al conectar con el servidor';
        console.error('Error:', error);
    });
});
