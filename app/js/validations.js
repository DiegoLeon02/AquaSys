function validateForm() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username === "" || password === "") {
        alert("Todos los campos son obligatorios.");
        return false;
    }
    return true;
}
