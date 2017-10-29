from apps import webapp
from flask import render_template
from apps import DBhelper
from flask import request
db = DBhelper.DB()
@webapp.route('/')
def home():
    return render_template('index.html')

@webapp.route('/viewlist')    
def viewlist():
    result = db.liststudent()
    return render_template('viewlist.html',result=result)
    
@webapp.route('/viewdetail')    
def  viewdetail():
    return "no" 

@webapp.route('/editstudent')           
def editstudent():
    return render_template('editstudent.html')

@webapp.route('/studentform')        
def studentform():
    return render_template('studentform.html')

@webapp.route('/addstudent', methods = ["POST","GET"])
def addstudent():
    db.addstudent(request.form.to_dict())
    return render_template('index.html')

def delete():
    return render_template('viewlist.html')

@webapp.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')
