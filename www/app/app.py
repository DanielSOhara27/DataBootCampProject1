from flask import Flask, render_template, request, jsonify
import www.app.dbController.dbConn as connector

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/amz200k-example')
def amz200k_example():
    return str(connector.exampleTable(1))


@app.route('/kindle-example')
def kindle_example():
    return str(connector.exampleTable(2))


@app.route('/students')
def students():

    return str(connector.find(debug=True))

@app.route('/addStudent', methods=['GET', 'POST'])
def addStudent():
    if request.method == "POST":
        details = request.form
        firstName = details['fname'] #Getting form data
        lastName = details['lname'] #Getting form data
        return connector.createStudent(firstName,lastName)

    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
