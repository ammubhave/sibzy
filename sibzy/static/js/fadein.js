function sizeSlideshow(){
        $('#main').height(($('html').height()-($('header').height()+$('footer').height()))+'px');

        //$('div.slider-nav span').css('margin-top',($('#intro').height()/2-50)+'px');
        $('section#intro').css('min-height',$('#main').height() - 100 + 'px');
}

$().ready(function() {
        
    sizeSlideshow(); 
        $('#intro').hide().fadeIn('slow');
        //$('#intro').hide().delay(1600).fadeIn('slow');
        $('#mission').hide().delay(1000).fadeIn('slow');
        $('.navbar').hide().delay(1600).fadeIn('slow');
        $('#home').hide().delay(1600).fadeIn('slow');
        $('#about').hide().delay(1600).fadeIn('slow');

        $(window).resize(sizeSlideshow);
});

$(document).ready(function(){
    $('section[data-type="background"]').each(function(){
        var $bgobj = $(this); // assigning the object
     
        $(window).scroll(function() {
            var yPos = -($window.scrollTop() / $bgobj.data('speed')); 
             
            // Put together our final background position
            var coords = '50% '+ yPos + 'px';
 
            // Move the background
            $bgobj.css({ backgroundPosition: coords });
        }); 
    });    
}); 