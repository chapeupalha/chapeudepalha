$(function () {

    $('.js-basic-example').DataTable({
        dom: 'Bfrtip',
        responsive: true,
        language: {
            "url": "//cdn.datatables.net/plug-ins/1.10.19/i18n/Portuguese-Brasil.json"
        }
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

});