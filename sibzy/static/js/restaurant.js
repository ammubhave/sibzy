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
                
            }
        });
    }
    console.log(path);
});