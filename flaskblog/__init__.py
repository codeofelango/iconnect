import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)



# Google Cloud SQL (change this accordingly)
PASSWORD ="root"
PUBLIC_IP_ADDRESS ="104.197.120.50"
DBNAME ="helpdeskdb"
PROJECT_ID ="atlantean-talon-162113"
INSTANCE_NAME ="atlantean-talon-162113:us-central1:herfysecongeneration-dev"



app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>



# configuration
# app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql + mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket =/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= True
 
# db = SQLAlchemy(app)




db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googleemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'elango.shunmugaraj@herfy.com'
app.config['MAIL_PASSWORD'] = '@herfy1234'

# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)
from flaskblog import routes


