var email = document.getElementById('email');
var password = document.getElementById('contraseña');
var error = document.getElementById('error');
error.style.color = 'red';

function enviarFormulario(){
    console.log('Enviando formulario...');

    var mensajesError = [];

    if (email.value === null || email.value === ''){
        mensajesError.push('Ingresa tu Email');
    }

    if (password.value === null || password.value === ''){
        mensajesError.push('Ingresa tu contraseña');

    }

    error.innerHTML = mensajesError.join(', ');

    return false;
}

var form = document.getElementById('formulario');
    form.addEventListener('submit', function(evt)){
        
    };
