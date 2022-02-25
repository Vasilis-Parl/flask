from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_bcrypt import Bcrypt

from flask_login import LoginManager


app = Flask(__name__)



app.config["SECRET_KEY"] = '0aabfe90b17540d5fd339411ce129035661471c1bd7b02eff0d3ab8e0876b2b5'
app.config['WTF_CSRF_SECRET_KEY'] = '5aa79ebeda1bac94e3f579d7b6490066c21224b23cdbd0143009ce58c21c8a4e'
### Configuration για τα Secret Key, WTF CSRF Secret Key, SQLAlchemy Database URL, 
## Το όνομα του αρχείου της βάσης δεδομένων θα πρέπει να είναι 'flask_movies_database.db'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flask_movies_database.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


### Αρχικοποίηση της Βάσης, και άλλων εργαλείων ###
### Δώστε τις σωστές τιμές παρακάτω ###

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

login_manager.login_view = "login_page"
login_manager.login_message_category = "warning"
login_manager.login_message = "Παρακαλούμε κάντε πρώτα είσοδο για να μπορέσετε να δείτε αυτή τη σελίδα."


from flaskMoviesApp import routes , models



