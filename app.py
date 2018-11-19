
from flask import Flask,render_template,redirect,url_for,request,session,flash
from flask_sqlalchemy import SQLAlchemy 
from functools import wraps
from sqlalchemy import and_



app =Flask(__name__)
app.secret_key = "lol"
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lanschristopher:db@localhost/lanschristopher'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ybctpoxrjrgwfj:1854d630f94fae116c32c30abba59749712ece44e1a06f44aadfb30e183f298e@ec2-50-19-249-121.compute-1.amazonaws.com:5432/d7k933hmm55v1p'
db = SQLAlchemy(app)



class User(db.Model):
    
   
    ifsc = db.Column(db.String, unique=True, primary_key=True)
    bank_id = db.Column(db.String)
    branch = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)
    district = db.Column(db.String)
    state = db.Column(db.String)
    bank_name = db.Column(db.String)

    def __init__(self, ifsc, bank_id, branch, address, city, district, state, bank_name):
        self.ifsc = ifsc
        self.bank_id = bank_id
        self.branch = branch
        self.address = address
        self.city = city
        self.district = district
        self.state = state
        self.bank_name = bank_name

    
    def __repr__(self):
       
        return 'IFSC : {} BANK ID : {} BRANCH : {} ADDRESS : {} CITY : {} DISTRICT : {} STATE : {} BANK NAME : {} '.format(self.ifsc,self.bank_id,self.branch,self.address,self.city,self.district,self.state,self.bank_name)

        


@app.route('/')
def home():
   
    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
    
    meh = 'True'
    myUser=None
    error = None
    if request.method == 'POST':
        myUser =  User.query.filter_by(ifsc=request.form['ifsc']).first()
        
        meh = 'False'
        if myUser == None:
            meh = 'True'
            error = 'No records found.'
        return render_template("search.html", myUser = myUser , meh = meh, error = error)
    else:
        return render_template("search.html", myUser = myUser , meh = meh )


@app.route('/search1', methods=['GET', 'POST'])
def search1():
    meh = 'True'
    myUser=None
  
    error = None
    if request.method == 'POST':
        
        
       
        myUser =  User.query.filter(and_(User.bank_name==request.form['name'],User.city==request.form['city'])).all()
      
        meh = 'False'
        if myUser == None:
            meh = 'True'
            error = 'No records found.'
        
        return render_template("search1.html", myUser = myUser , meh = meh ,error = error)
    else:
        return render_template("search1.html", myUser = myUser , meh = meh)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Credentials donot match. Please Try agian'
        else:
            session['logged_in'] = True
            flash("HEY")
            error = 'Login Successful'
            return redirect(url_for('search'))
        
    return render_template("login.html", error = error)

@app.route('/logout')
def logout():
    session.pop('logged_in',None)
    return redirect(url_for('/'))



if __name__ == '__main__':
    app.run(debug=True)