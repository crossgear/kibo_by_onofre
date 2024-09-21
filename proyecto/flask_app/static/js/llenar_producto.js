document.addEventListener("DOMContentLoaded", () => {

});

function completar_informacion(id){
    fetch('/obtener_producto/'+id)
        .then( response => response.json() )
        .then( async data =>  {
            $("option").each(function(){
                $(this).removeAttr('selected');;
            });
            $("#nombre_producto").val(data["nombre"])
            $("#descripcion").val(data["descripcion"])
            $("#precio").val(data["precio"])
            $("#stock_ideal").val(data["stock_ideal"])
            $("#stock_disponible").val(data["stock_disponible"])
            $("#stock_minimo").val(data["stock_minimo"])
            $("#descuento").val(data["descuento"])
            $('option:selected', this).remove();
            console.log("Marca: " + data["marca_id"])
            $("#marca  option[value='"+data["marca_id"]+"']").attr('selected', true);
            console.log("Categoria: " + data["categoria_id"])
            $("#categoria  option[value='"+data["categoria_id"]+"']").attr('selected', true);
            $("#id").val(data["id"])
    });
}
