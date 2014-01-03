#########
Templates
#########

==============
sibzy.frontend
==============

..  glossary::

    404.html
        The 404 Page not Found default template
    
    500.html
        The 500 Internal Server Error default template
        
    about.html
        **#!frontend/about**: The About us page
        
    base.html
        **/**: The Base parent template which is always shown. This contains JS code to load child templates.
        
    home.html
        **#!frontend/home**: The logged in home page
        
    landing.html
        **#!frontend/landing**: The not-logged in landing page
        
    theteam.html
        **#!frontend/theteam**: The Team section of the website

================
sibzy.restaurant
================

..  glossary::

    restaurant_profile.html
        **#!restaurant/profile/<restaurant id>**: The specific restaurant profile landing page. Contains code to load the details from the server.
        
============
sibzy.search
============

..  glossary::
    
    search_q.html
        **#!search/q/<query>**: Code to do a search and display search results    