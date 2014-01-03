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
                
                $('#search-result').append(item);
            }
        }
    })
})