
setTimeout(function(){
    $('.btn-savecard').click()
}, 500);


$(function () {
    $('.js-sweetalert button').on('click', function () {
        var type = $(this).data('type');

        if (type === 'prompt') {
            showPromptMessage();
        }
    });


});


function showPromptMessage() {
    swal({
        title: "Cadastre o cartão do participante",
        text: "Aproxime o cartão do leitor para efetuar o cadastro",
        type: "input",
        showCancelButton: true,
        closeOnConfirm: false,
        animation: "slide-from-top",
        inputPlaceholder: "Informações do cartão"
    }, function (inputValue) {
        if (inputValue === false) return false;
        if (inputValue === "") {
            swal.showInputError("Você precisa aproximar o cartão para finalizar o cadastro"); return false
        } else {
            participante = $('.id_participante').val()
            obj_ajax = {}
            obj_ajax['csrfmiddlewaretoken'] = $('.token').find('input').val()
            obj_ajax['id_particip'] = participante
            obj_ajax['codcard'] = inputValue

            $.ajax({
                type: 'POST',
                url: '/participante/cadastro/'+participante+'/cardsave',
                dataType: "json",
                data: obj_ajax,
                success: function(data){
                    setTimeout(function(){ location.href="/participante"; }, 2000);
                }
            });
            swal("Cadastrado!", "", "success");
        }
    });
}
