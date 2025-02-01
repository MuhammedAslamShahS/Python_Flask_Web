from flask import Flask
app = Flask(__name__)


# Mian Page / Home page

@app.route('/')
def home():
    return "Hello world \n This is Home page"


# About page

@app.route('/about')
def about():
    return "This is About Page"


# Product page

@app.route('/product')
def product():
    return "This is Product Page"



# Product/laptop page

@app.route('/product/laptop')
def laptop():
    return "This is Product/laptop Page"


# Contact page

@app.route('/contact')
def contact():
    return "This is Contact Page"


# Add URL RULE
app.add_url_rule('/home', 'home', home)

if __name__ == '__main__':
    app.run(debug=True) 