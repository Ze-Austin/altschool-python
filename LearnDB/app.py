from crypt import methods
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

base_dir = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(base_dir, 'users.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(db.String(255), nullable=False)

    def __init__(self, username, email, age, gender):
        self.username = username
        self.email = email
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"User {self.username}"


@app.route('/')
def index():
    users = User.query.all()

    context = {
        'users':users
    }

    return render_template("models.html", **context)

# Creating a User
@app.route('/users', methods={'POST'})
def create_user():
    username = request.form.get('username')
    email = request.form.get('email')
    age = request.form.get('age')
    gender = request.form.get('gender')

    new_user = User(username=username, email=email, age=age, gender=gender)

    db.session.add(new_user)
    db.session.commit()
    
    return redirect(url_for('index'))

# Update route
@app.route('/update/<int:id>/', methods=['GET', 'POST'])
def update(id):
    user_to_update = User.query.get_or_404(id)

    if request.method == 'POST':
        user_to_update.username = request.form.get('username')
        user_to_update.email = request.form.get('email')
        user_to_update.age = request.form.get('age')
        user_to_update.gender = request.form.get('gender')

        db.session.commit()

        return redirect(url_for('index'))
    
    context = {
        'user': user_to_update
    }

    return render_template('update.html', **context)

# Delete
@app.route('/delete/<int:id>/', methods=['GET'])
def delete_user(id):
    user_to_delete = User.query.get_or_404(id)

    db.session.delete(user_to_delete)
    db.session.commit()

    return redirect(url_for('index'))
    

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)