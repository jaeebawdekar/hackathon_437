from flask import Flask
from flask import render_template
from flask import url_for,request,redirect,session,jsonify,url_for
from flask_login import UserMixin,login_user,LoginManager,login_required,logout_user,current_user
# from flask_sqlalchemy import SQLAlchemy
from tensorflow.keras.models import load_model
from flask_bcrypt import Bcrypt
import test
import train

app=Flask(__name__)
app.secret_key="jaee"
model = load_model('chatbot_model.model')
model_file_path = 'chatbot_model.model'

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/register")
def register():
    return render_template('register.html')


@app.route('/chatbot', methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        user_message = request.form.get('message', '')
        response = test.predict_response(user_message)
        return jsonify({'response': response})
    else:
        session['referrer_url'] = request.referrer
        return render_template('chatbot.html')

   
            
if(__name__=='__main__'):
    app.run(debug=True,port=5500)
        

        
        
         
            
                