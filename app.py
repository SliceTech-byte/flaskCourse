from flask import Flask, render_template

app = Flask(__name__)

# '/' -> home page
# '/home' -> home page

@app.route('/')
@app.route('/home')
def homePage():
    return render_template('home.html', title="Flask Course - Home Page", header="Home Page", text="You are at the home page")


@app.route('/contact')
def contactPage():
    return render_template('contact.html', title="Flask Course - Contact Page", header="Contact Page", 
    text="You are at the contact page")