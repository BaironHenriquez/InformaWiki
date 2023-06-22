function login() {
    var email = document.forms["form1"]["email"].value;
    var password = document.forms["form1"]["password"].value;
  
    if (email === "") {
      alert("Por favor, ingresa tu correo electrónico.");
      return false;
    }
  
    if (password === "") {
      alert("Por favor, ingresa tu contraseña.");
      return false;
    }
  
    
  
    return true;
  }
  
  document.querySelector(".register-link").addEventListener("click", function() {
    document.querySelector(".wrapper").classList.add("active");
  });
  
  document.querySelector(".login-link").addEventListener("click", function() {
    document.querySelector(".wrapper").classList.remove("active");
  });
  