from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
import www.app.dbController.dbConn as connector

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'dev'
app.config['MYSQL_PASSWORD'] = 'dev123'
app.config['MYSQL_DB'] = 'flaskTest'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname'] #Getting form data
        lastName = details['lname'] #Getting form data
        cur = mysql.connection.cursor() #Connector
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()

        return 'success'
    return render_template('test.html')


@app.route('/students', methods=['GET', 'POST'])
def students():

    if request.method == "POST":
        details = request.form
        test = details['test']
        scope = details['scope']

    return str(connector.find(debug=True))


if __name__ == '__main__':
    app.run(debug=True)
