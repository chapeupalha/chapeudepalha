$(function () {
    $('.js-basic-example').DataTable({
        responsive: true
    });

    //Exportable table
    $('.js-exportable').DataTable({
        dom: 'Bfrtip',
        responsive: true,
        buttons: [
    //        'copy', 'csv', 'excel', 'pdf', 'print'
            'csv', 'excel', 'pdf', 'print'
        ],
        language: {
            "url": "//cdn.datatables.net/plug-ins/1.10.19/i18n/Portuguese-Brasil.json"
        }
    });

    $('.js-modal-buttons .btn').on('click', function () {
        var color = $(this).data('color');
        $('#mdModal .modal-content').removeAttr('class').addClass('modal-content modal-col-' + color);
        $('#mdModal').modal('show');

        setTimeout(function(){
            $('.modal-content').click()
        }, 500);

    });

    $('.modal-content').on('click', function () {
        $('input[name=cartao_id]').focus();
    });

});
