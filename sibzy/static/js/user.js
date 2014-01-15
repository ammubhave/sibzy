$(function () {
    $.ajax ({
        url: '/!/comment/user',
        dataType: 'json',
        success: function (data) {
            $.each(data, function(index, comment) {
                var entry = $('._dish-details-comments-entry').clone();
                entry.removeClass('_dish-details-comments-entry');
                entry.removeClass('noshow');
                console.log(comment);
                entry.find('._dish-details-comments-entry-commenttext').text(comment.comment_text);
                
                entry.find('._dish-details-comments-entry-ratingvalue').html('');
                var i = 0;
                for (; i < comment.rating_value; i++) {
                    entry.find('._dish-details-comments-entry-ratingvalue').append($('<i class="glyphicon glyphicon-star"></i>'));
                }
                for (; i < 5; i++) {
                    entry.find('._dish-details-comments-entry-ratingvalue').append($('<i class="glyphicon glyphicon-star-empty"></i>'));
                }
                
                $('#user-comments').append(entry);
            });
        }
    });
});