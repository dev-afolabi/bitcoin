$(document).ready(function(){
    $('#bank_transfer').hide();
    $('#btc_transfer').hide();
    $('#id_payment_option_0').on('click', function(){
        $('#btc_transfer').hide();
        $('#bank_transfer').show();
    })
    $('#id_payment_option_1').on('click', function(){
        $('#btc_transfer').show();
        $('#bank_transfer').hide();
    })
})