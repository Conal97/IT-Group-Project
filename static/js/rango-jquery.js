$(document).ready(function() {

    // Get the text value of the selected option
    $('#munros').change(function() {
    var selected_munro = $('#munros').find(":selected").text();

    // Append the text value to the input field of the form
    var input = $("#id_bagged");
    input.val(input.val() + selected_munro + ",")
    })
});