from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def landing():
    return render_template('index.html')
@app.route('/ninja')
def ninja():
    return render_template('ninja.html', name= "Mina Daya", Desc= "Python Ninja",
    name1="Julia Dreyfus", desc1= "Java Ninja")
def dojos():
    return render_template("dojos.htm")
@app.route('/dojos/new', methods=['POST'])
def register():
    print "Got Post info"
    name = request.form['name']
    email = request.form['email']
    return redirect ('/dojos.html')
app.run(debug=True)
