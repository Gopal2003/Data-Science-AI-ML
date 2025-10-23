from flask import Flask,render_template,request

'''
 Creating the Instance of Flask Class,
 Which will be your WSGI (Web Server GateWay Interface) application.
 Web Server : Werkzeug server(Flask's built-in Web Server)

 render_template : This template is responsible to redirect to another page like HTML. It uses jinja2
 In Flask (Python), the request object is used to access data sent by the client (browser or API consumer) to your web application.
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
    #   return request.form

'''
debug=Ture automatically make the changes appear without the need of restart.
'''
if __name__ == "__main__":
    app.run(debug=True)