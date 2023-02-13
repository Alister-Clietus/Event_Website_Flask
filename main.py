from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:9495366284@localhost/datadb'
db = SQLAlchemy(app)

conn=mysql.connector.connect(host="localhost",user="root",password="9495366284",database="datadb")
cursor=conn.cursor

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(80), unique=True, nullable=False)
    Last_Name = db.Column(db.String(120), unique=True, nullable=False)
    Address = db.Column(db.String(120), unique=True, nullable=False)
    Gender = db.Column(db.String(120), unique=True, nullable=False)
    DOB = db.Column(db.String(120), unique=True, nullable=False)
    PINCODE = db.Column(db.Integer, unique=True, nullable=False)
    Course = db.Column(db.String(120), unique=True, nullable=False)
    Email_ID = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def homep():
    return render_template('home.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/login_validation',methods=['POST'])
def  login_validation():
    email1 = request.form.get('email')
    password = request.form.get('password')
    print(email1)
    print(password)
    cursor = conn.cursor()

    # Execute a query
    cursor.execute("SELECT * FROM users where Email_ID='%s'" %(email1,))
    # Fetch the results
    results = cursor.fetchall()
    print(results)

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Return the results
    return str(results)

@app.route('/add_user',methods=['POST'])
def add_user():

    firstname = request.form.get('firstname')
    lastname = request.form.get('lastname')
    address = request.form.get('address')
    gender = request.form.get('gender')
    dob = request.form.get('dob')
    pincode = request.form.get('pincode')
    course = request.form.get('course')
    email = request.form.get('email')
    sql = Users(First_Name=firstname, Last_Name=lastname, Address=address, Gender=gender, DOB=dob, PINCODE=pincode, Course=course, Email_ID=email)
    db.session.add(sql)
    db.session.commit()
    return render_template('home.html')


if __name__=="__main__":
    app.run(debug=True)