# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.
#
# The below has been auto-generated for your Flask project

import sys
import os
from dotenv import load_dotenv

# add your project directory to the sys.path
project_home = u'/home/bisterco/mysite'

# env
project_folder = os.path.expanduser('~/mysite')
load_dotenv(os.path.join(project_folder,'b.env'))

if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from flask_app import app as application  # noqa
