$(document).ready(function() {
    $('#like_btn_area').click(function() {
        var areaSlug;
        areaSlug = $(this).attr('data-areaslug');
        
        $.get('/rango/like_area/',
            {'area_slug': areaSlug},
            function(data) {
                $('#like_count').html(data);
                $('#like_btn_area').hide();
        })
    });

    $('#like_btn_munro').click(function() {
        var munroSlug;
        munroSlug = $(this).attr('data-munroSlug');
        
        $.get('/rango/like_munro/',
            {'munro_slug': munroSlug},
            function(data) {
                $('#like_count').html(data);
                $('#like_btn_munro').hide();
        })
    });

});
    