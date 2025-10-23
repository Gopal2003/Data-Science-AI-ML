from flask import Flask,render_template

'''
 Creating the Instance of Flask Class,
 Which will be your WSGI (Web Server GateWay Interface) application.
 Web Server : Werkzeug server(Flask's built-in Web Server)

 render_template : This template is responsible to redirect to another page like HTML. It uses jinja2
'''

app = Flask(__name__ ) # Web Application (WSGI)

@app.route("/")
def Welcome():
    return "<html><H3>Welcome to the Flask Course </H3></html>"

@app.route("/Index")
def WelcomeIndex():
    return render_template('index.html')

'''
debug=Ture automatically make the changes appear without the need of restart.
'''
if __name__ == "__main__":
    app.run(debug=True)