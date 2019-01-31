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
    #make sure they sent you data for "first"
    if "first" in request.form:
      session["first"] = request.form["first"]
    if "first" not in session:
      session.clear()
      return redirect(url_for('renderMain'))

    return render_template('page2.html')
       

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    #TODO: set the favorite color in the session
     if "second" in request.form:
      session["first"] = request.form["second"]
    if "second" not in session:
      session.clear()
      return redirect(url_for('renderMain'))

    return render_template('page3.html')
       

  
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
    #TODO: set the favorite color in the session
    session["third"] = request.form["third"] #adds the favorite color to the cookie
    if session["fourth"] == request.form["fourth"] and "fourth" not in session :
       return render_template('page4.html')
    else:
       session.clear()
       return redirect(url_for('renderMain'))

  
@app.route('/page5',methods=['GET','POST'])
def renderPage5():
    #TODO: set the favorite color in the session
    session["fourth"] = request.form["fourth"] #adds the favorite color to the cookie
    if session["fifth"] == request.form["fifth"] and session["fifth"] not in session:
       return render_template('page5.html')
    else:
       session.clear()
       return redirect(url_for('renderMain'))

  
@app.route('/page6',methods=['GET','POST'])
def renderPage6():
    #TODO: set the favorite color in the session
     session["fifth"] = request.form["fifth"] #adds the favorite color to the cookie
     score=0
     if session["first"]==2:
      score=score+1
     else:
      score=score+0
     if session["second"]==63:
      score=score+1
     else:
      score=score+0
     if session["third"]==125:
      score=score+1
     else:
      score=score+0
     if session["forth"]==5:
      score=score+1
     else:
      score=score+0
     if session["fifth"]=="c":
      score=score+1
     else:
      score=score+0
     print(score);
     return render_template('page6.html')

if __name__=="__main__":
    app.run(debug=True)
