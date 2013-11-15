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
pip install -r requirements.txt
python manage.py syncdb
```

In the end you will have a directory structure similar to this:
```
sibzy
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

```
python manage.py runserver
```
