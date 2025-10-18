from flask import Flask

'''
 Creating the Instance of Flask Class,
 Which will be your WSGI (Web Server GateWay Interface) application.
'''

app = Flask(__name__ )

@app.route("/")
def Welcome():
    return "Welcome To the Flask Course"

if __name__ == "__main__":
    app.run()