
document.addEventListener("DOMContentLoaded", () => {
    getData()
});


//codigo basado en esta pagina: https://www.sitepoint.com/delay-sleep-pause-wait/
function sleep(ms) {return new Promise(resolve => setTimeout(resolve, ms));}

function getData(){
    fetch('/process_notificaciones')
        .then( response => response.json() )
        .then( async data =>  {
            if (data.length > 0){
                let titulo = "Stock de Productos";
                let mensaje = ""
                if(data.length == 1){
                    mensaje = "Existe " + data.length  + " artículo con bajo stock"
                }else{
                    mensaje = "Existen " + data.length  + " artículos con bajo stock"
                }
                notificacion(titulo,mensaje)
            }
    });
}



function notificacion(titulo, mensaje){

    var propiedades = {
        body: mensaje,
        icon: "/static/images/icono_notificacion.png"
    }

    if(!("Notification" in window)){
        alert("El navegador no soporta notificaciones");
    }else if (Notification.permission === "granted"){
        var notificacion = new Notification(titulo, propiedades)

        notificacion.onclick = (ev) => {
            window.location.href = '/dashboard/reporte';
        }
        
    }else if( Notification.permission !== "denied"){
        Notification.requestPermission(function(permission){
            if (Notification.permission === "granted"){
                var notificacion = new Notification(titulo, propiedades) 
                notificacion.onclick = (ev) => {
                    window.location.href = '/dashboard/reporte';
                }
            }
        });
    }
}


