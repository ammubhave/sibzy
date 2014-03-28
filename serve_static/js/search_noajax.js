var map = null;
$(function() { 
   // var myLatlng = new google.maps.LatLng(restaurant.location.latitude, restaurant.location.longitude);
    var mapOptions = {
       // center: myLatlng,
        zoom: 17
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
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
    
    var data = json;
    for (var i = 0; i < data.length; i++) {
        var restaurant = data[i];
        
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
                
        
    }
})