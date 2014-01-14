var restaurant = {};

$(function () {
    path = document.location.hash.substring(2);//.substring(document.location.indexOf('#!') + 2)
    paths = path.split('/');
    
    if (paths[1] == 'profile') {
        $.ajax({
            url: '/!/restaurant/profile/' + paths[2],
            dataType: 'json',
            success: function (data) {
                console.log(data);
                $('.restaurant-name').text(data.name);
                $('#txtSearch').val(data.name);
                $('#txtSearch').click(function () {
                    $(this).val('');
                    $(this).unbind('click');
                })
                restaurant.name = data.name;
                
                $('.restaurant-location-latitude').text(data.location.latitude);
                $('.restaurant-location-longitude').text(data.location.longitude);
                $('.restaurant-location-address').text(data.location.address);
                $('.restaurant-location-city').text(data.location.city);
                $('.restaurant-location-state').text(data.location.state);
                $('.restaurant-location-country').text(data.location.country);
                $('.restaurant-location-phone').text(data.location.phone);
                restaurant.location = data.location;
                //$('#map-canvas').trigger('ondataload');
                
                $('.restaurant-rating-total').text(data.rating.total);
                $('.restaurant-rating-glutenfree').text(data.rating.glutenfree);
                $('.restaurant-rating-vegetarian').text(data.rating.vegetarian);
                $('.restaurant-rating-vegan').text(data.rating.vegan);
                $('.restaurant-rating-peanutfree').text(data.rating.peanutfree);
                $('.restaurant-rating-lactoseint').text(data.rating.lactoseint);
                $('.restaurant-rating-seafoodint').text(data.rating.seafoodint);
                
                // Restaurant Categories
                $('.restaurant-categories').text('');
                $.each(data.category, function(index, category) {
                    var item = null;
                    if (data.category.length == 1) {
                        item = $('._restaurant-categories-element').clone();
                        item.removeClass('._restaurant-categories-element');
                    }
                    if (index == 0) {
                        item = $('._restaurant-categories-element-start').clone();
                        item.removeClass('._restaurant-categories-element-start');
                    } else if (index == data.category.length - 1) {
                        item = $('._restaurant-categories-element-end').clone();
                        item.removeClass('._restaurant-categories-element-end');
                    } else {
                        item = $('._restaurant-categories-element').clone();
                        item.removeClass('._restaurant-categories-element');
                    }
                    
                    item.show();
                    
                    item.children('._restaurant-categories-element-name').text(category.name);
                    item.children('._restaurant-categories-element-slug').text(category.slug);
                    
                    $('.restaurant-categories').append(item);
                   
                });
                
                 
                    
                    // Rating
                    restaurant.rating = { };
                    restaurant.rating.total = parseFloat(data.rating.total);
                  // alert(data.rating.total);
                    $('._restaurant-rating-total').trigger('ondataload');
                    
                    restaurant.dishes = data.dishes;
                    $('._restaurant-dishes').trigger('ondataload');
            },
            error: function(data) {
                alert('404 Not Found');
            }
        });
    }
    console.log(path);
});

    $('#map-canvas').bind('ondataload', function() {
				//alert('load map');
				var myLatlng = new google.maps.LatLng(restaurant.location.latitude, restaurant.location.longitude);
				var mapOptions = {
					center: myLatlng,
					zoom: 17
				};
				var map = new google.maps.Map(document.getElementById("map-canvas"),
					mapOptions);
				
				var marker = new google.maps.Marker({
					position: myLatlng,
					map: map,
					title: restaurant.name,
				});
				var infowindow = new google.maps.InfoWindow({
					content: restaurant.name
				});
					google.maps.event.addListener(marker, 'click', function() {
					infowindow.open(map,marker);
				});
				
			});

$('#rating').bind('ondataload', function () { 
    $(this).css('width', (restaurant.rating.total * 20) + 'px' ) 
});

$('._restaurant-dishes').bind('ondataload', function() {
            
            $.each(restaurant.dishes, function(index, dish) {
                var entry = $('._restaurant-dishes-entry').clone();
                entry.show();
                //entry.css('background-color', 'grey');
                entry.unbind('click');
                entry.bind('click', function() {
                    //if ($('#dishinfo').css('display') == 'none') {
						$('#review').show();
                        $('#dishinfo').show();
                        $('.dishes-comments-new').show();
                        $('#dishes-comments-button').unbind('click');
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
