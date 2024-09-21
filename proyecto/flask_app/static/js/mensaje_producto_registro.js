document.addEventListener("DOMContentLoaded", () => {
  var myForm = document.getElementById('crear_producto');
  if (myForm != null){
    myForm.onsubmit = function(e){
      e.preventDefault();
      var errores = new Array();
      var form = new FormData(myForm);
      var is_valid = true

      if (form.get("nombre").length < 5){
        errores.push("El nombre debe tener al menos 5 caracteres.");
        is_valid = false
      }
      if (form.get("descripcion").length < 10){
        errores.push("La descripcion debe tener al menos 10 caracteres.")
        is_valid = false
      }

      if (form.get("precio") == "" || parseInt(form.get("precio")) < 100){
        errores.push("Fija un precio")
        is_valid = false
      }
      if (form.get("stock_ideal") == "" || parseInt(form.get("stock_ideal")) <= 0){
        errores.push("Fija el stock ideal")
        is_valid = false
      }

      var etiquetaError = document.querySelector("#error")
      if(!is_valid){
        etiquetaError.innerHTML = ""
        for(var i = 0; i < errores.length; i++){
          etiquetaError.innerHTML += "<li>" + errores[i] + "</li>"
        }
        var boxMensaje = document.querySelector(".mensaje")
        boxMensaje.style.display = "flex"
        errores = []
      }else{
        fetch("/process_producto", { method :'POST', body : form})
        .then(response => {
          if (response.redirected) {
            window.location.assign(response.url)
          } else {
            response.json().then(data => {
              etiquetaError.innerHTML = ""
              etiquetaError.innerHTML += "<li>" + data.mensaje + "</li>"
              var boxMensaje = document.querySelector(".mensaje")
              boxMensaje.style.display = "flex"
            });
          }
        })
      }
      
      var botonAceptar = document.querySelector("#aceptar");
      var boxMensaje = document.querySelector(".mensaje");
      botonAceptar.addEventListener("click", function () {
        boxMensaje.style.display = "none";
      });
  }
  }

  var myForm2 = document.getElementById('crear_categoria');
  if (myForm2 != null){
    myForm2.onsubmit = function(e){
      e.preventDefault();
      var error = "";
      var form = new FormData(myForm2);
      var is_valid = true

      if (form.get("nombre").length < 5){
        error = "El nombre debe tener al menos 3 caracteres.";
        is_valid = false
      }

      var etiquetaError = document.querySelector("#error")
      if(!is_valid){
        etiquetaError.innerHTML = ""
        etiquetaError.innerHTML += "<li>" + error + "</li>"
        var boxMensaje = document.querySelector(".mensaje")
        boxMensaje.style.display = "flex"
        error = ""
      }else{
        fetch("/process_categoria", { method :'POST', body : form})
        .then(response => {
          if (response.redirected) {
            window.location.assign(response.url)
          } else {
            console.log("Error")
          }
        })
      }
      
      var botonAceptar = document.querySelector("#aceptar");
      var boxMensaje = document.querySelector(".mensaje");
      botonAceptar.addEventListener("click", function () {
        boxMensaje.style.display = "none";
      });
  }
  }

  var myForm3 = document.getElementById('crear_marca');
  if (myForm3 != null){
    myForm3.onsubmit = function(e){
      e.preventDefault();
      var error = "";
      var form = new FormData(myForm3);
      var is_valid = true

      if (form.get("nombre").length < 5){
        error = "El nombre debe tener al menos 3 caracteres.";
        is_valid = false
      }

      var etiquetaError = document.querySelector("#error")
      if(!is_valid){
        etiquetaError.innerHTML = ""
        etiquetaError.innerHTML += "<li>" + error + "</li>"
        var boxMensaje = document.querySelector(".mensaje")
        boxMensaje.style.display = "flex"
        error = ""
      }else{
        fetch("/process_marca", { method :'POST', body : form})
        .then(response => {
          if (response.redirected) {
            window.location.assign(response.url)
          } else {
            console.log("Error")
          }
        })
      }
      
      var botonAceptar = document.querySelector("#aceptar");
      var boxMensaje = document.querySelector(".mensaje");
      botonAceptar.addEventListener("click", function () {
        boxMensaje.style.display = "none";
      });
  }
  }
  
});
