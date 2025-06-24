from flask import Flask

import os

app = Flask(__name__,
            template_folder=os.path.join('templates'),
            static_folder='static',
            static_url_path='/static')

# Disable caching of static files during development
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

from app import views  # to avoid circular imports
