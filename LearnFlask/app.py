# Module name: flask; Class name: Flask
from flask import Flask

app = Flask(__name__)

# / is the homepage
@app.route('/')
def hello_world():
    return "Hello world!"

# /subpage creates a static subpage
@app.route('/about')
def about():
    return "I am learning Flask with AltSchool."

# /<variable> makes the subpage dynamic. Use the variable within the function
@app.route('/<name>')
def greet_user(name):
    return f"Hello {name}! How are you doing?"

# /<datatype:variable> makes the route insist on given datatype
@app.route('/post/<int:id>')
def post_id(id):
    return f"This post has an ID of {id}"

# Live Class task
@app.route('/<name>/<birthmonth>/<birthday>')
def birthday(name, birthmonth, birthday):
    return f"{name} was born on {birthmonth} {birthday}."

if __name__ == "__main__":
    app.run(debug=True)