============
Colaborativa
============


Versions
========

- Python 3.5.2
- Django 2.2.15


Testing on Open edX
===================

sudo su edxapp -s /bin/bash
cd /edx/app/edxapp/edx-platform
source ../edxapp_env

python manage.py lms shell --settings production
from django.conf import settings
settings.INSTALLED_APPS
import colaborativa

python manage.py lms migrate colaborativa zero --settings production
python manage.py lms migrate colaborativa --settings production
python manage.py lms showmigrations colaborativa --settings production

pip install -U git+https://github.com/moinhos-colaborativa/django-colaborativa.git@feature/initial-form

LDFLAGS=-L/usr/lib/openssl-1.0 CFLAGS="-I/usr/include/openssl-1.0" pyenv install 3.5.2

/edx/app/edxapp/venvs/edxapp/lib/python3.5/site-packages/colaborativa/

sudo -H -u edxapp bash -c 'cd /edx/app/edxapp/ && source edxapp_env && cd edx-platform && paver update_assets --settings production'

References
==========

https://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/configuration/customize_registration_page.html
