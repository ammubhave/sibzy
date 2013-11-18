Sibzy
=====

Installation
------------

Navigate to the root repo directory
```
cd sibzy
sudo apt-get install $(< requirements.system)
```

Now navigate to any other directory which does not have a directory named sibzy

```
virtualenv sibzy
cd sibzy
source bin/activate
mkdir www
cp <the path to the sibzy repo directory> www -r
cd www/sibzy
pip install -r requirements.txt
python manage.py syncdb
```

In the end you will have a directory structure similar to this:
```
sibzy  (This will be referred to as the sibzy virtualenv folder)
  |-- bin
  |-- lib
  |-- local
  |-- www
  |    |-- sibzy
  |    |     |-- manage.py
  |    |     |-- requirements.txt
  |    |     |-- requirements.system
  |    |     |-- README.md
  |    |     |-- docs
  |    |     |     |-- --
  |    |     |-- sibzy
  |    |           |-- settings.py
  |    |           |-- --
             
```

Running
-------

Navigate to the sibzy virtualenv folder.
If you already activated the virtualenv (i.e. you have a (sibzy) written on the left of the command prompt) then you can directly cd to the sibzy repo directory.
```
source bin/activate
cd www/sibzy
python manage.py runserver
```
