from flask import Flask , render_template,request ,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from pymysql.err import OperationalError
from sqlalchemy.exc import OperationalError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'mysql+pymysql://root:@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db=SQLAlchemy(app)

class Users(db.Model):
    __tablename__ ="users"
    id = db.Column(db.Integer,primary_key = True)
    username=db.Column(db.String(100))
    email=db.Column(db.String(100))
    password=db.Column(db.String(100))
    
@app.route('/listuser')
def list_user():
    user = Users.query.first() 
    return f"username : {user.username}"

@app.route('/listalluser')
def list_alluser():
    user = Users.query.all() 
    return render_template("users.html", user=user)


@app.route('/')
def user_register():
    return render_template('/register.html')

@app.route('/register', methods =['GET','POST'])
def register_user():
    if request.method == 'POST':
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        
        new_user = Users(username=username , email=email , password=password )    
        db.session.add(new_user)
        db.session.commit()
        # return "Data inserted."
    return render_template('/register.html')

@app.route('/updateuser/<int:id>')
def updateuser(id):
    user=user.query.get(id)
    return render_template('updateuser.html',user=user)

@app.route('/update',methods=["POST"])
def update(id):
 user=Users.query.get(id)
 user.username=request.form['username']
 user.email=request.form['email']
 user.u_password=request.form['password']
 db.session.add(user)
 db.session.commit()
 return redirect('/listalluser')
 

@app.route('/deleteuser/<int:id>')
def deleteuser(id):
     user=Users.query.get(id)
     if user:
         db.session.delete(user)
         db.session.commit()
         return redirect('/listalluser')
    # user=Users.query.get_or_404(id)

# @app.route('/')    
# def check_connection():
# def check_connection():
#     try:
#         db.session.execute(text("SELECT * from user"))
#         return "Connection to MySQL database successful!"
#     except OperationalError as e:
#         return f"Connection failed: {str(e)}"
    
#create an application to collect a visitor information of pokhara university.application should collect following information.
#visitor name,address,contact number,gender,purpose of visit,visit date,visit time,concerned department.also list all the visitor
#information on table.


class Visitors(db.Model):
    __tablename__ ="visitor"
    Id = db.Column(db.Integer,primary_key = True)
    Name=db.Column(db.String(100))
    Address=db.Column(db.String(100))
    Contact=db.Column(db.String(100))
    Gender=db.Column(db.String(100))
    Description=db.Column(db.String(100))
    Date=db.Column(db.String(100))
    Time=db.Column(db.String(100))
    Department=db.Column(db.String(100))
    
@app.route('/information',methods=['GET','POST'])
def information():
    new_visit=Visitors(
    Name=request.form['Name'],
    Address=request.form['Address'],
    Contact=request.form['Contact'],
    Gender=request.form['Gender'],
    Description=request.form['Description'],
    Date=request.form['Date'],
    Time=request.form['Time'],
    Department=request.form['Department']
    )
   
    db.session.add(new_visit)
    db.session.commit()
    return render_template('/info.html')

@app.route('/listallvisitor')
def list_allvisitor():
    visit = Visitors.query.all() 
    return render_template("visit_info.html", visit=visit)
  
if __name__=='__main__':
    app.run(debug=True)
