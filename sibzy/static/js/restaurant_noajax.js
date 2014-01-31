var restaurant = {};

var comments_xhr = null;
function load_comments(id) {
    $('#dish-details-comments').html('');
    if (comments_xhr) {
	comments_xhr.abort();
	comments_xhr = null;
    }
    comments_xhr = $.ajax({
	url: '/!/comment/dish/' + id,
	dataType: 'json',
	success: function(data) {
	    comments_xhr = null;
	    //console.log(data);
	    $.each(data, function(index, comment) {
		if (comment.user.id == user_id) {
		    rate = comment.rating_value;
		    for (var j=1; j<=rate;j++) {
			$('#rate'+j).removeClass('glyphicon-star-empty');
			$('#rate'+j).addClass('glyphicon-star');
		    }
		    for (var j=rate+1; j<=5;j++) {
			$('#rate'+j).removeClass('glyphicon-star');
			$('#rate'+j).addClass('glyphicon-star-empty');
		    }
		    $('#dishes-comments-text').val(comment.comment_text);
		} else {
		    var entry = $('._dish-details-comments-entry').clone();									
		    entry.show();
		    entry.removeClass('_dish-details-comments-entry');
		    console.log(comment);
		    entry.find('._dish-details-comments-entry-ratingvalue').text(comment.rating_value);
		    for (var j=1; j<=comment.rating_value;j++) {
			entry.find('.rrate'+j).removeClass('glyphicon-star-empty');
			entry.find('.rrate'+j).addClass('glyphicon-star');
		    }
		    entry.find('._dish-details-comments-entry-commenttext').text(comment.comment_text);
		    entry.find('._dish-details-comments-entry-user').text(comment.user.fbusername);	
		    $('#dish-details-comments').append(entry);
		}
	    });
	}
    })
}

$('._restaurant-dishes').bind('ondataload', function() {
            
            $.each(restaurant.dishes, function(index, dish) {
                var entry = $('._restaurant-dishes-entry').clone();
				entry.removeClass('_restaurant-dishes-entry');
                entry.show();
                //entry.css('background-color', 'grey');
                entry.unbind('click');
                entry.bind('click', function() {
                    //if ($('#dishinfo').css('display') == 'none') {
						$('#review').show();
                        $('#dishinfo').show();
                        $('.dishes-comments-new').show();
                        $('#dishes-comments-button0').unbind('click');
						$('#dishes-comments-button1').unbind('click');
						$('#dishes-comments-button2').unbind('click');
						$('#dishes-comments-button3').unbind('click');
						$('#dishes-comments-button4').unbind('click');
						$('#dishes-comments-button5').unbind('click');
						var comment_fn = function(val) {
							$.ajax({
                                method: 'POST',
                                url: '!/comment/dish/' + dish.id + '/new',
                                data: {
                                    'comment_text': $('#dishes-comments-text').val(),
                                    'rating_value': val
                                },
                                dataType: 'json',
                                success: function(data) {
                                    entry.trigger('click');
                                }
                            });
						};
                        $('#dishes-comments-button0').bind('click', function() { comment_fn(0); });
						$('#dishes-comments-button1').bind('click', function() { comment_fn(1); });
						$('#dishes-comments-button2').bind('click', function() { comment_fn(2); });
						$('#dishes-comments-button3').bind('click', function() { comment_fn(3); });
						$('#dishes-comments-button4').bind('click', function() { comment_fn(4); });
						$('#dishes-comments-button5').bind('click', function() { comment_fn(5); });
                        
                        $('#dish-details-name').text(dish.name);
						
						$('#dish-details-rating-stars').html('');
						var i = 0;
						for (; i < dish.rating; i++) {
							$('#dish-details-rating-stars').append($('<i class="glyphicon glyphicon-star"></i>'));
						}
						for (; i < 5; i++) {
							$('#dish-details-rating-stars').append($('<i class="glyphicon glyphicon-star-empty"></i>'));
						}
						
                        $('#dish-details-comments').html('');
                        $.ajax({
                            url: '!/comment/dish/' + dish.id,
                            dataType: 'json',
                            success: function(data) {
                                //console.log(data);
                                $.each(data, function(index, comment) {
                                    var entry = $('._dish-details-comments-entry').clone();									
                                    entry.show();
                                    entry.removeClass('_dish-details-comments-entry');
                                    console.log(comment);
                                    entry.find('._dish-details-comments-entry-ratingvalue').text(comment.rating_value);
                                    entry.find('._dish-details-comments-entry-commenttext').text(comment.comment_text);
                                    entry.find('._dish-details-comments-entry-user').text(comment.user.fbusername);
                                    entry.find('._dish-details-comments-entry-picture').attr('src', 'http://graph.facebook.com/' + comment.user.fbusername + '/picture?type=square&type=large');
                                    $('#dish-details-comments').append(entry);
                                });
                            }
                        })
                    
                    /*} else {
                        
                        $('#dishinfo').hide();
                        $('.restaurants-comments-new').show();
                        $('.dishes-comments-new').hide();
                    }*/
                });
                entry.find('._restaurant-dishes-entry-name').text(dish.name);
                entry.find('._restaurant-dishes-entry-price').text(dish.price);
                //console.log(dish.categories);
                if ($.inArray('Entree', dish.categories) > -1) {                    
                    $('#panelEntrees').append(entry);
                    //alert(dish.name);
                } else if ($.inArray('Appetizer', dish.categories) > -1) {
                    $('#panelAppetizers').append(entry);
                    //alert(dish.name);
                } else if ($.inArray('Desert', dish.categories) > -1) {                 
                    $('#panelDeserts').append(entry);
                    //alert(dish.name);
                } else {
                    $('#panelOthers').append(entry);
                }
                
            });
        });
