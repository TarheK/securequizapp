import os
from flask import Flask, url_for, render_template, request
from flask import redirect
from flask import session

app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# See: http://flask.pocoo.org/docs/0.10/quickstart/#sessions

app.secret_key=os.environ["SECRET_KEY"]; #This is an environment variable.  
                                     #The value should be set in Heroku (Settings->Config Vars).  

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    #TODO: delete everything from the session
    session.clear()
    return redirect(url_for('renderMain')) # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    #TODO: set the first and last name in the session
    session["firstName"] = request.formed["firstName"] #adds the first name to the cookie
    session["lastName"] = request.formed["lastName"] #adds the last name to the cookie
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    #TODO: set the favorite color in the session
     session["favoriteColor"] = request.formed["favoriteColor"] #adds the favorite color to the cookie
     return render_template('page3.html')
    
if __name__=="__main__":
    app.run(debug=False)
