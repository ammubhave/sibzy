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
                
                if (!(newpath in c))
                {
                    newpaths = newpath.split('/')
                    
                    //console.log(elem.attr('href').substring(1) + '-');
                    $.get('/!/' + newpaths[0] + '/load/' + newpaths[1], function( data ) {
                        c[newpaths[0] + '/' + newpaths[1]] = data;
                    }).fail( function(data){
                        //get the status code
                        console.log(data);
                        c[newpaths[0] + '/' + newpaths[1]] = data.responseText;
                    });
                    //console.log(elem.attr('href').substring(1) + '-');
                }
            }
        });
}
function navigate(path) {    
    paths = path.split('/')
    
    window.location = './#!' + path;
    if (path.indexOf('?') != -1) {
        path = path.substring(0, path.indexOf('?'));
    }
    if ((paths[0] + '/' + paths[1]) in c) {
        $('#content').remove();
        $('#content_parent').html($('<div>').attr('id', 'content'));
        
        $("#content" ).html( c[paths[0] + '/' + paths[1]] );
        //console.log($('#content a[href]'));
        
        activate_links();
    } else {
        $.ajax({
            url: '/!/' + paths[0] + '/load/' + paths[1],
            success: function( data ) {
                c[paths[0] + '/' + paths[1]] = data;
                navigate(path);
            },
            error: function(xhr, status, error) {
                c[paths[0] + '/' + paths[1]] = xhr.responseText;
                navigate(path);
            }
        });
    }
}

$(function () {
    if (window.location.hash == '') {
        navigate('frontend/landing');
    } else {
        navigate(window.location.hash.substring(2));        
    }
    $('#txtSearch').keyup(function (data) {
        q = $('#txtSearch').val();
        console.log(q)
        if (q == '') {
            navigate('frontend/home');
        } else {
            $.getJSON('/!/search/' + encodeURIComponent(q), function( data ) {
                navigate('frontend/search');
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
