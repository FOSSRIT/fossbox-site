"""
Author: Remy D <remyd@civx.us>
        Ralph Bean <rbean@redhat.com>
        Sam Lucidi <mansam@csh.rit.edu>
License: AGPL
"""
import os

from flask import Flask
from flask.ext.mako import MakoTemplates, render_template
from flask import redirect, url_for

app = Flask(__name__)
app.template_folder = "templates"
mako = MakoTemplates(app)


@app.route('/')
def index():
    return render_template('index.html', nam='mako')


@app.route('/about')
def about():
    return render_template('about.mak', name='mako')


if __name__ == "__main__":
    if 'OPENSHIFT_PYTHON_IP' in os.environ:
        host = os.environ['OPENSHIFT_PYTHON_IP']
        port = int(os.environ['OPENSHIFT_PYTHON_PORT'])
        app.run(host=host, port=port)
    else:
        app.debug = True
        app.run()
