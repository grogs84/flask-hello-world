# ----Flask Hello World---

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
	