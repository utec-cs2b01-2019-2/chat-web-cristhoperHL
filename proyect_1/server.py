from flask import Flask ,request ,make_response,redirect,render_template ,url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
import os


dbdir="sqlite:///" + os.path.abspath(os.getcwd()) + "/database.db"

app = Flask(__name__)
db=SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"]=dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
class Users(db.Model):
    id= db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(30),unique=True,nullable=False)
    email=db.Column(db.String(50),unique=True,nullable=False)
    password=db.Column(db.String(80),nullable=False)

@app.route('/sign up',methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        hashed_pw = generate_password_hash(request.form["password"],method="sha256")#sha256 es un metodo de cifrado 
        new_user = Users(username=request.form["username"],email=request.form["email"],password=hashed_pw)#paso todo a la base de datos
        return "Felicidades ya te registraste"

    return render_template('registrarse.html')

@app.route('/')
def index():
    return render_template('home.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('error_404.html',error=error)
    
@app.route('/blog')
def blog():
    return render_template('blog_1.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=="POST":
        user=Users.query.filter_by(username=request.form["username"]).first()
        if user and check_password_hash(request.form["password"],user.password):
            return render_template('blog_1.html')
        else:
            return render_template('login.html')
    return render_template('login.html')




if __name__ == '__main__':
    db.create_all()
    app.run(debug=True,port=8000)