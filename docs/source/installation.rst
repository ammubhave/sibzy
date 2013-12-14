############
Installation
############

Download the source code from Github

HTTPS clone URL: https://github.com/ammubhave/sibzy.git

SSH clone URL: git@github.com:ammubhave/sibzy.git

Subversion clone URL: https://github.com/ammubhave/sibzy

***********************
Development Environment
***********************

Clone repository
================

Clone the Git repository using the following command::

    git clone git@github.com:ammubhave/sibzy.git
  
This will create a directory called sibzy which will be the repository root directory

Installing system-wide requirements
===================================

::

    cd sibzy/requirements
    cat base.system | sudo apt-get install
    cat dev.system | sudo apt-get install
    sudo pip install virtualenv
    sudo pip install virtualenvwrapper
    echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
    source ~/.bashrc
    
    
You should now have system-wide dependencies installed.

Installing virtual environment and local dependencies
=====================================================
::

    mkvirtualenv sibzy
    pip install -r dev.txt
    
Now you should have all the python local dependencies installed.

Configuring database
====================

We will create a file called .my.cnf in your home directory (if you don't already have one) which will hold our db settings

*.my.cnf* ::

    [client]
    user=<mysql db user>
    password=<mysql db password>
    
Create a MySQL database called **sibzy** by opening a terminal::

    $ mysql -u <mysql db user> -p
    Enter Password: <mysql db password>
    
    mysql> create database sibzy;
    Query OK, 1 row affected
    
    mysql> exit
    Bye

You should now have created a database named sibzy.

Configuring envionment variables
================================

We will now configure the environment variables. Open a terminal::

    echo 'SECRET_KEY="<some random secret key>"' >> ~/.virtualenvs/sibzy/bin/activate
    
Running a server
================
Open a terminal window.

If you see *(sibzy)* written on the left side of the prompt then you have an active virtual environment.

If you do not see the *(sibzy)* prompt, type ``workon sibzy`` to activate the virtual environment

Navigate to the directory where **manage.py** file is located and run ``python manage.py runserver --settings=sibzy.settings.dev``

You should have a server running at **http://localhost:8000/**

If you want to terminate the server, just press Ctrl+C 

**********************
Production Environment
**********************

The production environment consists of an Apache2 server and a MySQL server. Apache uses the mod_wsgi module to serve wsgi.py file residing in the sibzy folder.

We use the following Apache configuration::

    <VirtualHost *:80>
        <Directory /home/ubuntu/sibzy/>
            Options Indexes FollowSymLinks MultiViews
            AllowOverride None
            Order allow,deny
            allow from all
        </Directory>

        WSGIScriptAlias / /home/ubuntu/sibzy/sibzy/sibzy/wsgi.py

    </VirtualHost>

