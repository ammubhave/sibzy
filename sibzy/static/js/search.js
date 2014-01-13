$(function() {
    path = document.location.hash.substring(2);
    paths = path.split('/');
    
    query = decodeURIComponent(paths[2]);
    
    $('.search-query').text(query);
    
   // var myLatlng = new google.maps.LatLng(restaurant.location.latitude, restaurant.location.longitude);
    var mapOptions = {
       // center: myLatlng,
        zoom: 17
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);
    
    var marker = new google.maps.Marker({
      //  position: myLatlng,
        map: map,
       // title: restaurant.name,
    });
    
    
    
    $.ajax({
        url: '/!/search/q/' + encodeURIComponent(query),
        dataType: 'json',
        success: function(data) {
            $('#search-result').html('');
            for (var i = 0; i < data.length; i++) {
                var restaurant = data[i];
                
                var item = $('#search-data-item').clone();
                item.css('display', '');
                item.find('.restaurant-name').text(restaurant.name);
                
                item.find('.restaurant-location-latitude').text(restaurant.location.latitude);
                item.find('.restaurant-location-longitude').text(restaurant.location.longitude);
                item.find('.restaurant-location-address').text(restaurant.location.address);
                item.find('.restaurant-location-city').text(restaurant.location.city);
                item.find('.restaurant-location-state').text(restaurant.location.state);
                //item.find('.restaurant-link').attr('href', '#!restaurant/profile/' + restaurant.id);
                
                var myLatlng = new google.maps.LatLng(restaurant.location.latitude, restaurant.location.longitude);
                marker = new google.maps.Marker({
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

                if (i == 0) {                    
                    map.setCenter(myLatlng);
                }
                
                item.mouseenter(function() {
                    $(this).removeClass('bs-callout-info');
                    $(this).addClass('bs-callout-warning');
                    
                    var myLatlng = new google.maps.LatLng(restaurant.location.latitude, restaurant.location.longitude);
                    
                    map.setCenter(myLatlng);
                    
                    
                    
                }).mouseleave(function () {
                    $(this).removeClass('bs-callout-warning');
                    $(this).addClass('bs-callout-info');
                }).click(function () {
                    navigate('restaurant/profile/' + restaurant.id);
                });
                
                
                
                $('#search-result').append(item);
                
            }
            activate_links();
        }
    })
})