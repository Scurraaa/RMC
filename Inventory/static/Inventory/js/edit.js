$(document).ready(function(){
    $('#select_model_number').click(function(event){
        event.preventDefault();
        var model_number = $('#select_model_number :selected').val();
        $.ajax({
            url: '/dashboard/inventory/edit_stocks/get_stock',
            type: "POST",
            data: {
                "model_number": model_number,
                "csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val(),
            },
            dataType: 'json',
            success: function(data){
                $('#current_stocks').val(data.stocks);
            },
            error: function (data) {
                $('#current_stocks').val(0);
            }
        });
    });
    $('#submit_stock').click(function(event){
        alert("Stocks Updated Successfully!");
        event.preventDefault();
        var stock = $('#current_stocks').val();
        var model_number = $('#select_model_number :selected').val();
        $.ajax({
            url: '/dashboard/inventory/edit_stocks/update',
            type: "POST",
            data: {
                "model_number": model_number,
                "stock": stock,
                "csrfmiddlewaretoken": $("input[name='csrfmiddlewaretoken']").val(),
            },
            dataType: 'json',
            success: function(data){
                if (data.status === "success") {
                    window.location.replace('/dashboard/inventory/')
                }
            },
            error: function (data) {
            }
        });
    });
});