$(document).ready(function() {
    $('#loginForm').submit(function(event) {
        event.preventDefault();
        var username = $('#username').val();
        var password = $('#password').val();
        var storedUsername = localStorage.getItem('username');
        var storedPassword = localStorage.getItem('password');
        var errorMessage = $('#errorMessage');
        if (username === storedUsername && password === storedPassword) {
            errorMessage.hide();
            window.location.href = 'index.html';
        } else {
            errorMessage.show();
        }
    });
});