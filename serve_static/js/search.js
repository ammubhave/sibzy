$(function() {
    path = document.location.hash.substring(2);
    paths = path.split('/');
    
    query = decodeURIComponent(paths[2]);
    
    $('.search-query').text(query);
    
    $.ajax({
        url: '/!/search/q/' + encodeURIComponent(query),
        dataType: 'json',
        success: function(data) {
            $('#search-result').html('');
            for (var i = 0; i < data.length; i++) {
                var restaurant = data[i];
                
                var item = $('#search-data-item').clone();
                item.css('display', '');
                item.children('.restaurant-name').text(restaurant.name);
                
                item.children('.restaurant-location-latitude').text(restaurant.location.latitude);
                item.children('.restaurant-location-longitude').text(restaurant.location.longitude);
                item.children('.restaurant-location-address').text(restaurant.location.address);
                item.children('.restaurant-location-city').text(restaurant.location.city.name);
                item.children('.restaurant-location-state').text(restaurant.location.state);
                
                $('#search-result').append(item);
            }
        }
    })
})