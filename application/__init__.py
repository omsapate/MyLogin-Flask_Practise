from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.secret_key = "vbnv5575vnvn84gn74g5h55s43srxe28795eeh"
app.config['MONGODB_SETTINGS'] = {
    'db': 'MYLOGIN'
}

db = MongoEngine()
db.init_app(app)

from application import routes