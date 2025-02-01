from flask import Flask, render_template
app = Flask(__name__)


# Mian Page / Home page

@app.route('/')
def home():
    return render_template('index.html')


# About page

@app.route('/about')
def about():
    return render_template('about.html')


# Product page

@app.route('/product')
def product():
    return render_template('product.html')



# Product/laptop page

@app.route('/product/laptop')
def laptop():
    return render_template('product.html')


# Contact page

@app.route('/contact')
def contact():
    return render_template('contact.html')


# Add URL RULE
app.add_url_rule('/home', 'home', home)

if __name__ == '__main__':
    app.run(debug=True) 