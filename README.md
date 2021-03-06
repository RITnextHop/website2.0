NextHop.Network 2.0 Source Code
===

Setup Env
---
Follow this guide to setup Python 3.6 and Pip. (Virtual Environment not necessary)

https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-centos-7

Setup NTP
---

NTP is needed to ensure releasing of events and such is accurates

*assuming centos 7*

    timedatectl set-ntp true

    timedatectl set-timezone America/New_York
    
    yum install -y ntpd

    systemctl enable ntpd

    systemctl start ntpd

Configure Data
---
The 'Initial Data' directory contains a yaml file of initial website data such as Club Info, Eboard, Past Events, etc. If this file is not imported a superuser must be created and Club Info and eboard must be populated for index page to load.

### Easy Way Out

In project root directory run these two commands

    chmod +x deploy.sh

    ./deploy.sh


### Do it yourself

To intialize the website with data and a superuser, run the below commands from the project root directory. 

    rm -rf db.sqlite3

    python3.6 manage.py migrate 

    python3.6 manage.py migrate --run-syncdb
    
    #for nexthop site data
    python3.6 manage.py loaddata Initial\ Data/initial_data_v2.yaml
    
    #for nsic site data
    python3.6 manage.py loaddata Initial\ Data/nsic_data.yaml

Run Test Server
---
In root dir of project run

    python3.6 manage.py runserver 0.0.0.0:8000
