$(document).ready(function(){
    $("#filtrar").on("click", function() {
        var min = $('#min').val();
        var max = $('#max').val();
        console.log(min);
        console.log(max);
        $("section .card").each(function() {
            var a = $(this).find(".precio_total").text();
            console.log(a)
            if (parseInt(a)<=max & parseInt(a)>=min){
                $(this).show();
            }
            else{
                $(this).hide();
            }
        });
    });
});
