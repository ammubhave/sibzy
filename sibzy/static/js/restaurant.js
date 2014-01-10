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
                    $('#rating').trigger('ondataload');
                    
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