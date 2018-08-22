$(document).ready(function(){

    function clrErrors(){
        $(".is-invalid").each(function(index, el){
            $(this).removeClass("is-invalid")
        })
    }

    $("#login-form").submit(function(e){
        clrErrors()
        if($("#username").val() == ""){
            $("#username").addClass("is-invalid")
            $("#inv-username").html("Insira um nome de usuário.")
            e.preventDefault()
        }
        else if($("#password").val() == ""){
            $("#password").addClass("is-invalid")
            $("#inv-password").html("Insira sua senha.")
            e.preventDefault()
        }
    })
})