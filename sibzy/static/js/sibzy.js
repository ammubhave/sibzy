var c = {}
function activate_links() {
    $('a[href]').each(function (index, elem) {
           //22 alert('y');
            elem = $(elem);
            var newpath = elem.attr('href').substring(1);
            newpath = newpath.substring(0, newpath.indexOf('?'));
            
            //console.log(elem);
            if (elem.attr('href').indexOf('#') == 0 && elem.attr('href').length > 1) {
                elem.unbind('click');
                elem.click(function(e){
                    $(this).unbind('click');
                    //$(this).remove();
                    e.preventDefault();
                    //console.log($(this).context.hash);
                    navigate(elem.attr('href').substring(1));
                    return false;
                });
                
                if (!(newpath in c)) {
                    
                    //console.log(elem.attr('href').substring(1) + '-');
                    $.get('/api/load/' + elem.attr('href').substring(1), function( data ) {
                        c[elem.attr('href').substring(1)] = data;
                    }).fail( function(data){
                        //get the status code
                        console.log(data);
                        c[elem.attr('href').substring(1)] = data.responseText;
                    });
                    //console.log(elem.attr('href').substring(1) + '-');
                }
            }
        });
}
function navigate(path) {
    window.location = './#' + path;
    if (path in c) {
        $('#content').remove();
        $('#content_parent').html($('<div>').attr('id', 'content'));
        
        $( "#content" ).html( c[path] );
        
        //console.log($('#content a[href]'));
        
        activate_links();
    } else {
        $.get('/api/load/' + path, function( data ) {
            c[path] = data;
            navigate(path);
        });
    }
}

$(function () {
    if (window.location.hash == '') {
        navigate('home');
    } else {
        navigate(window.location.hash.substring(1));
    }
    $('#txtSearch').keyup(function (data) {
        q = $('#txtSearch').val();
        console.log(q)
        if (q == '') {
            navigate('home');
        } else {
            $.getJSON('/api/search/' + encodeURIComponent(q), function( data ) {
                navigate('search');
                $('.search_q').text(q);
                
                $.each( data, function( index, r ) {
                    console.log(r);
                    $('#search_results').append($('<a href="#restaurant_profile?id=' + r['id'] + '"><h2>' + r['name'] + '</h2></a>'));
                });
                activate_links();
            });            
        }        
    });
});