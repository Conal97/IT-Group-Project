$(document).ready(function() {
    $('#like_btn_area').click(function() {
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
        )

        //hide button
        $('#like_btn_area').hide();
  
    });

    $('#unlike_btn_area').click(function() {
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
        )

        //hide button
        $('#unlike_btn_area').hide();
        
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
