###################
Directory Structure
###################

*****************************
Repository Root Structure (/)
*****************************

..  glossary::

    docs
        This directory contains all documentation related files. The final html documentation is available at docs/build/html/index.html. The Sphinx source code resides in docs/build/source directory
    
    requirements
        This directory contains the lists of required system packages and python packages.
        
        | *System package Requirements:* base.system, dev.system, prod.system
        | *Python PIP Requirements:* base.txt, dev.txt, prod.txt
        
    serve_static
        Should not be touched or modified directly. This directory holds all static files which are generated using `python manage.py collectstatic` command and hence should not be modified directly. This folder is only to be used in production environment for service static files. Do not run collectstatic in a development envionment otherwise it will mess up things production static files.
        
    sibzy
        The project root directory. Holds all source code for the website.

*******************************
Project Root Structure (/sibzy)
*******************************

..  glossary::
    
    backend
        This app forms an interface between the outisde world and internal source code. It handles service AJAX pages and HTML snapshots, handles DB queries made from urls and other stuff.
        
    frontend
        This app handles content which is actually seen by the user. Handles rendering of the home page and customization for different devices.
        
    sibzy
        This is the project configuration directory. It holds settings for development and production environment and the master url server.
        
    static
        Holds all the static files required for serving. This directory is accessible to the world via /static url.
        
    templates
        Holds all templates required. Also holds customization for administration section.

