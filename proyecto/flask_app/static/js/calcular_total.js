document.addEventListener("DOMContentLoaded", () => {
    let total = 0
    $(".subtotales").each(function(){
        total += Number($(this).text());
    });
    $("#total").text(total + " Gs.")

    fetch('https://dolar.melizeche.com/api/1.0/')
        .then(response => response.json())
        .then(json =>  $("#amount").val(total/((json.dolarpy.cambioschaco.venta+json.dolarpy.cambioschaco.compra)/2))
        )
});


function desaparecerboton(){
    var boxMensaje = document.querySelector(".mensaje_flash");
    boxMensaje.remove()
}