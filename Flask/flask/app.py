from flask import Flask

'''
 Creating the Instance of Flask Class,
 Which will be your WSGI (Web Server GateWay Interface) application.
 Web Server : Werkzeug server(Flask's built-in Web Server)
'''

app = Flask(__name__ ) # Web Application (WSGI)

@app.route("/")
def Welcome():
    return "Welcome To the Flask Course... "

@app.route("/Index")
def WelcomeIndex():
    return "Welcome To the Index Page... "

'''
debug=Ture automatically make the changes appear without the need of restart.
'''
if __name__ == "__main__":
    app.run(debug=True)