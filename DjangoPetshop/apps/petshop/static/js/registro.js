$(document).ready(function () {
    $('#registerForm').submit(function (event) {
        event.preventDefault();
        var newUsername = $('#newUsername').val();
        var newPassword = $('#newPassword').val();
        localStorage.setItem('username', newUsername);
        localStorage.setItem('password', newPassword); // Guardar la contraseña
        alert('Registro exitoso. Redirigiendo al inicio de sesión...');
        window.location.href = 'login.html';
    });
});