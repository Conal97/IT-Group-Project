$(document).ready(function() {

    // When user clicks like or unlike button on area page
    $('#like_btn_area, #unlike_btn_area').click(function() {
        var areaSlug;
        var username;
        var likeUnlike;
        areaSlug = $(this).attr('data-areaslug');
        username = $(this).attr('data-username');
        likeUnlike = $(this).attr('data-likeunlike');
        
        // add 1 to like then show on view
        $.get('/rango/like_area/',
            {'area_slug': areaSlug, 'like_unlike' : likeUnlike},
            function(data) {
                //with result from get request, update html with new data
                $('#like_count').html(data); 
        })

        // create new user likes area instance and update has liked boolean
        $.get('/rango/user_likes_area/',
            {'area_slug': areaSlug, 'user_name': username, 'like_unlike' : likeUnlike},
            function(data) {
                if (data) {
                    // if button has disable class remove it, otherwise add
                    if( $('#like_btn_area').hasClass("d-none") ){
                        $('#like_btn_area').removeClass("d-none");
                        $('#unlike_btn_area').addClass("d-none");
                    } else {
                        $('#like_btn_area').addClass("d-none");
                        $('#unlike_btn_area').removeClass("d-none");
                    }
                   
                } else{

                    if( $('#like_btn_area').hasClass("d-none") ){
                        $('#like_btn_area').removeClass("d-none");
                        $('#unlike_btn_area').addClass("d-none");
                    } else {
                        $('#like_btn_area').addClass("d-none");
                        $('#unlike_btn_area').removeClass("d-none");
                    }
                }
        })      
    });

    // When user clicks like or unlike button on munro page
    $('#unlike_btn_munro, #like_btn_munro').click(function() {
        var munroSlug;
        var username;
        var likeUnlike;
        munroSlug = $(this).attr('data-munroslug');
        username = $(this).attr('data-username');
        likeUnlike = $(this).attr('data-likeunlike');
        
        $.get('/rango/like_munro/',
            {'munro_slug': munroSlug, 'like_unlike' : likeUnlike},
            function(data) {
                $('#like_count_munro').html(data);
        })
         // create new user likes munro instance and update has liked boolean
         $.get('/rango/user_likes_munro/',
         {'munro_slug': munroSlug, 'user_name': username, 'like_unlike' : likeUnlike},
         function(data) {
            if (data) {
                // if button has disable class remove it, otherwise add
                if( $('#like_btn_munro').hasClass("d-none") ){
                    $('#like_btn_munro').removeClass("d-none");
                    $('#unlike_btn_munro').addClass("d-none");
                } else {
                    $('#like_btn_munro').addClass("d-none");
                    $('#unlike_btn_munro').removeClass("d-none");
                }
               
            } else{

                if( $('#like_btn_munro').hasClass("d-none") ){
                    $('#like_btn_munro').removeClass("d-none");
                    $('#unlike_btn_munro').addClass("d-none");
                } else {
                    $('#like_btn_munro').addClass("d-none");
                    $('#unlike_btn_munro').removeClass("d-none");
                }
            }
     })   
    });

    // If user searches something in area search bar, find area suggestions and load back to html
    $('#search-input').keyup(function() {
        var query;
        query = $(this).val();
        
        $.get('/rango/suggest/',
            {'suggestion': query},
            function(data) {
                //update areas-listing div
                $('#areas-listing').html(data);
        })
    });

});
