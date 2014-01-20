var c = {}, rs = {};
var was_search = false;
var last_search_q = '';

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var usrlocation = {
    'lat': 0,
    'lng': 0,
};
function sendLocToServer(position) {
    usrlocation.lat = position.coords.latitude;
    usrlocation.lng = position.coords.longitude;
    console.log(navigator.geolocation && getCookie('lat') === null);
    $.ajax({
        url: '/!/search/set_location',
        dataType: 'json',
        data: usrlocation,
    });
}

if (navigator.geolocation && getCookie('lat') === null) {
    navigator.geolocation.getCurrentPosition(sendLocToServer);
    console.log(navigator.geolocation);
} else {
    console.log("Geolocation is not supported by this browser.");
}

$(function () {
    $('#txtSearch').keyup(function (e) {
       var code = (e.keyCode ? e.keyCode : e.which);
      if(code == 13) {
        window.location = '/search/q/' + encodeURIComponent($('#txtSearch').val());
      }
      return false;
    });
});
