$(function () {
    path = document.location.hash.substring(2);//.substring(document.location.indexOf('#!') + 2)
    paths = path.split('/')
    ;
    if (paths[1] == 'profile') {
        $.ajax({
            url: '/!/restaurant/profile/' + paths[2],
            dataType: 'json',
            success: function (data) {
                console.log(data);
                $('.restaurant-name').text(data.name);
                $('.restaurant-location-latitude').text(data.location.latitude);
                $('.restaurant-location-longitude').text(data.location.longitude);
                $('.restaurant-location-address').text(data.location.address);
                $('.restaurant-location-city').text(data.location.city);
                $('.restaurant-rating-total').text(data.rating.total);
                $('.restaurant-rating-glutenfree').text(data.rating.glutenfree);
                $('.restaurant-rating-vegetarian').text(data.rating.vegetarian);
                $('.restaurant-rating-vegan').text(data.rating.vegan);
            }
        });
    }
    console.log(path);
});