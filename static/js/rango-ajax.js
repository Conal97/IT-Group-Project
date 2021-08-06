$(document).ready(function() {
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
                $('#like_count').html(data); 
        })

        // create new user likes area instance and update has liked boolean
        $.get('/rango/user_likes_area/',
            {'area_slug': areaSlug, 'user_name': username, 'like_unlike' : likeUnlike},
            function(data) {
                if (data) {
                    //if liked, hide like button
                    $('#like_btn_area').hide();
                    $('#unlike_btn_area').hide();
                } else{
                    //if liked, hide like button
                    $('#like_btn_area').hide();
                    $('#unlike_btn_area').hide();
                }
        })      
    });

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
                 //if liked, hide like button
                 $('#like_btn_munro').hide();
                 $('#unlike_btn_munro').hide();
             } else{
                 //if liked, hide like button
                 $('#like_btn_munro').hide();
                 $('#unlike_btn_munro').hide();
             }
     })   
    });

});
