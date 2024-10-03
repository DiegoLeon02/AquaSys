function validateForm() {
    var title = document.getElementById('title').value;
    var description = document.getElementById('description').value;
    var file = document.getElementById('file').value;

    if (title === "" || description === "" || file === "") {
        alert("Todos los campos son obligatorios.");
        return false;
    }

    var allowedExtensions = /(\.pdf)$/i;
    if (!allowedExtensions.exec(file)) {
        alert("Por favor, sube un archivo en formato PDF.");
        return false;
    }

    return true;
}
