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

Clone the Git repository using thw following command::

    git clone git@github.com:ammubhave/sibzy.git
  
This will create a directory called sibzy which will be the repository root directory.

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


