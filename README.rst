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

python manage.py lms showmigration colaborativa --settings production


References
==========

https://edx.readthedocs.io/projects/edx-installing-configuring-and-running/en/latest/configuration/customize_registration_page.html
