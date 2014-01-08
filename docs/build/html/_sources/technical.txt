#####################
Technical Information
#####################

*******************
Dynamic CSS Classes
*******************

..  glossary::
    
    .fb-login
        The element is visible only when the user is logged in.
        
    .fb-nologin
        The element is visible only when is not logged in.
        
    .fb-name
        The innerText is set to the user's full name
    
    .fb-username
        The innerText is set to the user's username
        
/restaurant
===================

..  glossary::

    .restaurant-name
        The name of the restaurant
    
    .restaurant-location-latitude
        The latitude
    
    .restaurant-location-longitude
        The longitude
        
    .restaurant-location-address
        The street address
        
    .restaurant-location-city
        The city
        
    .restaurant-location-state
        The state
    
    .restaurant-location-country
        The country
        
    .restaurant-location-phone
        The phone number
        
    .restaurant-rating-total
        The total rating
        
    .restaurant-rating-glutenfree
        The glutenfree rating
    
    .restaurant-rating-vegetarian
        The vegetarian rating
        
    .restaurant-rating-vegan
        The vegan rating
        
    .restaurant-rating-peanutfree
        The peanutfree rating
        
    .restaurant-rating-lactoseint
        The lactose intolerant rating
        
    .restaurant-rating-seafoodint
        The seafood intolerant rating
        
    .restaurant-categories
        The restaurant categories. This element will contain copies of ._restaurant-categories-element
        
    ._restaurant-categories-element
        Internal. Copies of this element will populate .restaurant-categories
    
    ._restaurant-categories-element-name
        Internal. Inside ._restaurant-categories-element. Category name
    
    ._restaurant-categories-element-slug
        Internal. Inside ._restaurant-categories-element. Category slug
        
******
How to
******

How to login?
=============

Call FB.login() by setting onclick

How to logout?
==============

Call FB.logout() by settins onclick
