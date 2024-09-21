document.addEventListener("DOMContentLoaded", () => {
  var myForm = document.getElementById('actualizar_producto');
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
        fetch("/process_actualizar_producto", { method :'POST', body : form})
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
