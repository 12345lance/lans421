from app import db
from app import User
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ybctpoxrjrgwfj:1854d630f94fae116c32c30abba59749712ece44e1a06f44aadfb30e183f298e@ec2-50-19-249-121.compute-1.amazonaws.com:5432/d7k933hmm55v1p'
db = SQLAlchemy(app)
db.create_all()
db.session.add(User("ABSDCAAAS11","60","ABHYUDAYA NAGAR","ABHYUDAYA EDUCATION SOCIETY, OPP. BLDG. NO. 18, ABHYUDAYA NAGAR, KALACHOWKY, MUMBAI - 400033","MUMBAI","GREATER MUMBAI","MAHARASHTRA","ABHYUDAYA COOPERATIVE BANK LIMITED"))
db.session.commit()

#print "hello"