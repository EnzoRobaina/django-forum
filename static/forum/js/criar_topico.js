$(document).ready(function(){

    function clrErrors(){
        $(".is-invalid").each(function(index, el){
            $(this).removeClass("is-invalid")
        })
    }

    $("#submit-topico").click(function(){
        clrErrors()
    }) 
})