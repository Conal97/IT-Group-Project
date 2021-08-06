$(document).ready(function() {

    $('#munros').change(function() {
    var selected_munro = $('#munros').find(":selected").text();

    var input = $("#id_bagged");
    input.val(input.val()+selected_munro + ",")
    })
});