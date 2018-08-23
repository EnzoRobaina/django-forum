$(document).ready(function(){

    function clrErrors(){
        $(".is-invalid").each(function(index, el){
            $(this).removeClass("is-invalid")
        })
    }

    $("form").submit(function(e){
        clrErrors()
        if($("#titulo").val() == ""){
            $("#titulo").addClass("is-invalid")
            $("#inv-titulo").html("Insira um título.")
            e.preventDefault()
        }
        else if($("#id_texto").val() == ""){
            $("#inv-texto").html("Insira um texto.")
            e.preventDefault()
        }
    })
})