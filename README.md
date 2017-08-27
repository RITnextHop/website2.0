NextHop.Network 2.0 Source Code
===

Setup Env
---
Follow this guide to setup Python 3.6 and Pip. (Virtual Environment not neccissary)

https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7

Configure Data
---
The 'Initial Data' directory contains a yaml file of initial website data such as Club Info, Eboard, etc. This file must be imported for the index page to load. Otherwise 

    rm -rf db.sqlite3

    python3.6 manage.py migrate 

    python3.6 manage.py migrate --run-syncdb
    
Run Test Server
---
In root dir of project run

    python3.6 manage.py runserver 0.0.0.0:8000
