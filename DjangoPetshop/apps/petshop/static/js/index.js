document.addEventListener('DOMContentLoaded', function() {
    const username = localStorage.getItem('username');
    const accountContainer = document.getElementById('accountContainer');
    if (username) {
        accountContainer.innerHTML = `
            <a class="navbar-brand nav-link dropdown-toggle navbar-link navbar_texto" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Cuenta
            </a>
            <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Perfil</a></li>
                <li><a class="dropdown-item" href="#" id="logoutLink">Cerrar Sesión</a></li>
            </ul>
        `;
    } else {
        accountContainer.innerHTML = `
            <a class="btn btn-primary" href="login.html">Log In</a>
        `;
    }
    const logoutLink = document.getElementById('logoutLink');
    if (logoutLink) {
        logoutLink.addEventListener('click', function(event) {
            event.preventDefault();
            localStorage.removeItem('username');
            alert('Sesión cerrada correctamente.');
            window.location.href = 'index.html';
        });
    }
});