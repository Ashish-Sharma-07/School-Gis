# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

# Django settings for the GeoNode project.
import os
from geonode.settings import *
#
# General Django development settings
#
PROJECT_NAME = 'my_school'

# per-deployment settings should go here
SITEURL = os.getenv('SITEURL',"http://localhost:8000/")
SITENAME = 'my_school'

# SECRET_KEY = '************************'
# Make this unique, and don't share it with anybody.
SECRET_KEY = os.getenv('SECRET_KEY', "hbpd2gp8@fa*a6l9o8kn%)r9+j#2e+3_^n)_of@zr#jhx@6a$$")

# Defines the directory that contains the settings file as the LOCAL_ROOT
# It is used for relative settings elsewhere.
LOCAL_ROOT = os.path.abspath(os.path.dirname(__file__))

WSGI_APPLICATION = "{}.wsgi.application".format(PROJECT_NAME)

ALLOWED_HOSTS = ['localhost', 'django'] if os.getenv('ALLOWED_HOSTS') is None \
    else re.split(r' *[,|:|;] *', os.getenv('ALLOWED_HOSTS'))

# Location of url mappings
ROOT_URLCONF = os.getenv('ROOT_URLCONF', '{}.urls'.format(PROJECT_NAME))

USE_JSONFIELD = True

# this should be overriden in your my_school.local_settings
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    'sqlite:///{path}'.format(
        path=os.path.join(LOCAL_ROOT, 'development.db')
    )
)

# Defines settings for development
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
}

INSTALLED_APPS += (PROJECT_NAME,)

INSTALLED_APPS += ("jsonfield",)

MEDIA_ROOT = os.getenv('MEDIA_ROOT', os.path.join(LOCAL_ROOT, "uploaded"))

STATIC_ROOT = os.getenv('STATIC_ROOT',
                        os.path.join(LOCAL_ROOT, "static_root")
                        )

# Additional directories which hold static files
STATICFILES_DIRS.append(
    os.path.join(LOCAL_ROOT, "static"),
)

# Location of locale files
LOCALE_PATHS = (
    os.path.join(LOCAL_ROOT, 'locale'),
    ) + LOCALE_PATHS

TEMPLATES[0]['DIRS'].insert(0, os.path.join(LOCAL_ROOT, "templates"))
loaders = TEMPLATES[0]['OPTIONS'].get('loaders') or ['django.template.loaders.filesystem.Loader','django.template.loaders.app_directories.Loader']
# loaders.insert(0, 'apptemplates.Loader')
TEMPLATES[0]['OPTIONS']['loaders'] = loaders
TEMPLATES[0].pop('APP_DIRS', None)
