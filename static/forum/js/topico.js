$(document).ready(function(){

    $("form").submit(function(e){

        if($("#id_texto").val() == ""){
            $("#inv-texto").html("<b>Insira um texto.</b>")
            e.preventDefault()
        }
    })
})