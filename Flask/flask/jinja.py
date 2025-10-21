from flask import Flask,render_template,request,redirect,url_for

'''
 Creating the Instance of Flask Class,
 Which will be your WSGI (Web Server GateWay Interface) application.
 Web Server : Werkzeug server(Flask's built-in Web Server)

 render_template(Function) : This template is responsible to redirect to another page like HTML. It uses jinja2
'''

app = Flask(__name__ ) # Web Application (WSGI)

@app.route("/")
def Welcome():
    return "<html><H3>Welcome to the Flask Course </H3></html>"

@app.route("/index",methods=['GET'])
def WelcomeIndex():
    return render_template('index.html')


@app.route('/form',methods=['GET','post'])
def form():
    if request.method == 'POST':
        # print(type(request.form))
        name = request.form['user_name']
        return name
    return render_template('form.html')

# Variable Rule
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    exp = {'score' : score,'res':res}
    return render_template('result1.html',result = exp)


@app.route('/successif/<int:score>')
def successif(score):

    return render_template('result.html',result = score)

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    # render_template('getresult.html')
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science + maths + data_science + c) / 4
    else:
        return render_template('getresult.html')
    return redirect(url_for('success',score=total_score))

'''
debug=Ture automatically make the changes appear without the need of restart.
'''
if __name__ == "__main__":
    app.run(debug=True)