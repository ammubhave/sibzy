var c = {}, rs = {};

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

function show_restaurant_details(id) {
    //console.log(rs[id].name);
    $('#restaurant_name').text(rs[id].name);
}

function activate_links() {
    $('a[href]').each(function (index, elem) {
           //22 alert('y');
            elem = $(elem);
            var newpath = elem.attr('href').substring(2);         
            
            
            //console.log(elem);
            if (elem.attr('href').indexOf('#!') == 0 && elem.attr('href').length > 1) {
                
                newpath = newpath.substring(0, newpath.indexOf('?'));
                
                
                elem.unbind('click');
                elem.click(function(e){
                    $(this).unbind('click');
                    //$(this).remove();
                    e.preventDefault();
                    //console.log($(this).context.hash);
                    navigate(elem.attr('href').substring(2));
                    
                    if (newpath == 'restaurant_profile') {
                        show_restaurant_details(elem.attr('href').substring(elem.attr('href').indexOf('?id=') + 4));
                    }
                    
                    return false;
                });
                
                if (!(newpath in c)) {
                    
                    //console.log(elem.attr('href').substring(1) + '-');
                    $.get('/!/load/' + elem.attr('href').substring(2), function( data ) {
                        c[elem.attr('href').substring(2)] = data;
                    }).fail( function(data){
                        //get the status code
                        console.log(data);
                        c[elem.attr('href').substring(2)] = data.responseText;
                    });
                    //console.log(elem.attr('href').substring(1) + '-');
                }
            }
        });
}
function navigate(path) {    
    
    
    window.location = './#!' + path;
    if (path.indexOf('?') != -1) {
        path = path.substring(0, path.indexOf('?'));
    }
    if (path in c) {
        $('#content').remove();
        $('#content_parent').html($('<div>').attr('id', 'content'));
        
        $("#content" ).html( c[path] );
        
        //console.log($('#content a[href]'));
        
        activate_links();
    } else {
        $.get('/!/load/' + path, function( data ) {
            c[path] = data;
            navigate(path);
        });
    }
}

$(function () {
    if (window.location.hash == '') {
        navigate('landing');
    } else {
        navigate(window.location.hash.substring(2));        
    }
    $('#txtSearch').keyup(function (data) {
        q = $('#txtSearch').val();
        console.log(q)
        if (q == '') {
            navigate('home');
        } else {
            $.getJSON('/!/search/' + encodeURIComponent(q), function( data ) {
                navigate('search');
                $('.search_q').text(q);
                
                $.each( data, function( index, r ) {
                    rs[r['id']] = r;
                    $('#search_results').append($('<a href="#restaurant_profile?id=' + r['id'] + '"><h2>' + r['name'] + '</h2></a>'));
                });
                activate_links();
            });            
        }        
    });
    
    $.ajaxSetup({
        headers: { 'X-CSRFToken': getCookie('csrftoken') }
    }); 
});
