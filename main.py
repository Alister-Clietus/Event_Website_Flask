from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def about():
    return render_template('home.html')

@app.route('/admin')
def about():
    return render_template('admin.html')


if __name__=="__main__":
    app.run(debug=True)