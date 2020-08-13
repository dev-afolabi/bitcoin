$(document).ready(function(){
    $('#bank_transfer').hide();
    $('#btc_transfer').hide();
    $('#id_payment_option_0').on('click', function(){
        $('#btc_transfer').hide();
        $('#id_wallet_address').val("");
        $('#bank_transfer').show();
        
    })
    $('#id_payment_option_1').on('click', function(){
        $('#btc_transfer').show();
        $('#bank_transfer').hide();
        $('#id_bank_name').val("");
        $('#id_account_number').val("");
        $('#id_swift_code').val("");
        $('#id_IBAN_number').val("");
    })
})