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
     if "first" in session:
      session.clear()
      return redirect(url_for('renderMain'))
     if "first" in request.form:
      session["first"] = request.form["first"]
     return render_template('page2.html')
       

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    #TODO: set the favorite color in the session
     if "second" in session:
      session.clear()
      return redirect(url_for('renderMain'))
     if "second" in request.form:
      session["second"] = request.form["second"]
     return render_template('page3.html')
       

  
@app.route('/page4',methods=['GET','POST'])
def renderPage4():
     if "third" in session:
      session.clear()
      return redirect(url_for('renderMain'))
     if "third" in request.form:
      session["third"] = request.form["third"]
     return render_template('page4.html')
       

@app.route('/page5',methods=['GET','POST'])
def renderPage5():
     if "fourth" in session:
      session.clear()
      return redirect(url_for('renderMain'))
     if "fourth" in request.form:
      session["fourth"] = request.form["fourth"]
     return render_template('page5.html')
       
  
@app.route('/page6',methods=['GET','POST'])
def renderPage6():
     if "fifth" in session:
      session.clear()
      return redirect(url_for('renderMain'))
     if "fifth" in request.form:
      session["fifth"] = request.form["fifth"]
     return render_template('page6.html')
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
    if session["fourth"]==5:
      score=score+1
    else:
      score=score+0
    if session["fifth"]=="4":
      score=score+1
    else:
      score=score+0
    print(score);
    return render_template('page6.html')
    return score

if __name__=="__main__":
    app.run(debug=True)
