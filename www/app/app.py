# 1. Import Flask.
from flask import Flask, jsonify

myDictionary = {"name":"Flask", "version":"0.01", "status":"development"}

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Define what to do when a user hits the index route
@app.route("/", methods=['GET','POST'])
def home():
    print("Server received request for 'Home' page")
    return "Welcome to my API with Json responses!"

# 4. Define what to do when a user hits the /about route
@app.route("/normal")
def normal():
    print("Server received a request for the 'normal response' page")
    return myDictionary

@app.route("/json")
def json():
    print("Server received request for 'Contact' page")
    return jsonify(myDictionary)

if __name__ == "__main__":
    app.run(debug=True)
