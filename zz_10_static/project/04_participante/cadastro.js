//
// setTimeout(function(){
//     $('.btn-savecard').click()
// }, 500);


$(document).ready(function() {
    $('#id_dt_nascimento').bootstrapMaterialDatePicker({
        lang: 'pt-br',
        time: false,
        clearButton: true,
        format: 'DD/MM/YYYY',
        cancelText: 'Descartar',
        clearText: 'Limpar',
    });

    $('#id_dt_entrada').bootstrapMaterialDatePicker({
        lang: 'pt-br',
        time: false,
        clearButton: true,
        format: 'DD/MM/YYYY',
        cancelText: 'Descartar',
        clearText: 'Limpar',
    });

    $('#id_dt_saida').bootstrapMaterialDatePicker({
        lang: 'pt-br',
        time: false,
        clearButton: true,
        format: 'DD/MM/YYYY',
        cancelText: 'Descartar',
        clearText: 'Limpar',
    });

    $('#id_representante_legal_dt_nascimento').bootstrapMaterialDatePicker({
        lang: 'pt-br',
        time: false,
        clearButton: true,
        format: 'DD/MM/YYYY',
        cancelText: 'Descartar',
        clearText: 'Limpar',

    });

    $('.form-line').on('change', '#id_documento', function() {
        if($(this)[0].files[0].type != "application/pdf") {
            $(this)[0].value = ''
            alert('O arquivo de cada Recibo deve ser em .PDF')
        }
    });

    $('.fone_input').inputmask('(99) 99999-9999', { placeholder: '(__) _____-____' });
    $('.cpf_input').inputmask('999.999.999-99', { placeholder: '___.___.___-__' });
    $('.cep_input').inputmask('99999-999', { placeholder: '_____-___' });
    $('.date_input').inputmask('dd/mm/yyyy', { placeholder: '__/__/____' });

});

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
