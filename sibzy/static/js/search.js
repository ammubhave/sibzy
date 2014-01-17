

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
    
    if (getCookie('lat') != null) { 
        var myLatlng = new google.maps.LatLng(getCookie('lat'), getCookie('lng'));
                    var marker = new google.maps.Marker({
                        position: myLatlng,
                        map: map,
                        title: "You",
                        icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
                    });
                    var infowindow = new google.maps.InfoWindow({
                        content: "Your location"
                    });
                    google.maps.event.addListener(marker, 'click', function() {
                        infowindow.open(map,marker);
                    });
                    
    }
    $.ajax({
        url: '/!/search/q/' + encodeURIComponent(query),
        dataType: 'json',
        success: function(data) {
            $('#txtSearch').val(query);
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
                    var marker = new google.maps.Marker({
                        position: myLatlng,
                        map: map,
                        title: restaurant.name,
                        icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png',
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
                    marker.setIcon('http://maps.google.com/mapfiles/ms/icons/green-dot.png');
                    
                    
                }).mouseleave(function () {
                    $(this).removeClass('bs-callout-warning');
                    $(this).addClass('bs-callout-info');
                    marker.setIcon('http://maps.google.com/mapfiles/ms/icons/red-dot.png');
                }).click(function () {
                    was_search = true;
                    last_search_q = $('#txtSearch').val();
                    
                    navigate('restaurant/profile/' + restaurant.id);
                });
                
                
                
                $('#search-result').append(item);
                
            }
            activate_links();
        }
    })
})