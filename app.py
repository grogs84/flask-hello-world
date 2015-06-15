# ----Flask Hello World---

# my new note on 6/15/2015 2:48pm

# import the Flask class from the flask
from flask import Flask


# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route("/")
@app.route("/home")
def hello_world():
	return "Hello, World!"

# start the development server using run() method
if __name__ == "__main__":
	app.run()
	