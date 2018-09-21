$(function () {
    $('.datepicker').bootstrapMaterialDatePicker({
        format: 'DD/MM/YYYY',
        clearButton: false,
        weekStart: 1,
        time: false,
        cancelText: 'Descartar',
        clearText: 'Limpar'
    });
});