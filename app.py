from flask import Flask, render_template, request
import os
app = Flask(__name__)


# for app configuration
app.config['UPLOAD_PATH'] = 'static/images'

# Mian Page / Home page
@app.route('/')
def home():
    return render_template('index.html')

# Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        number = request.form.get('number')
        email = request.form.get('email')
        return render_template('register.html', name=name, number=number, email=email)
    return render_template('index.html')

# Upload File
@app.route('/upload', methods = ['POST'])
def upload():
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename))
    return 'uploaded successfully'



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