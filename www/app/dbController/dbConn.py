# https://dev.mysql.com/doc/connectors/en/connector-python-api-errors.html
from flask import g
from www.app.dbController import host, user, pwd, db, dbTest
import mysql.connector
from datetime import datetime, date
from ast import literal_eval

_connection_prod = mysql.connector.connect(
            database=db,
            host=host,
            user=user,
            passwd=pwd,
            auth_plugin='mysql_native_password'
        )

_connection_debug = mysql.connector.connect(
            database=db,
            host=host,
            user=user,
            passwd=pwd,
            auth_plugin='mysql_native_password'
        )


def startconnection(debug=True):
    myDB = db

    if debug:
        myDB = dbTest

    if 'db' not in g:
        mySql = mysql.connector.connect(
            database=myDB,
            host=host,
            user=user,
            passwd=pwd
        )

    return mySql.cursor()


def getCol(scope, columnScope='all'):
    if columnScope == 'all':
        return ['*']

    if int(scope) == 1:

        if int(columnScope) == 1:
            return ['amz_id', 'Item ID', 'Review Time', 'Rating', 'Summary', 'Review Text']
        else:
            return ['Item ID', 'Review Time', 'Rating']
    elif int(scope) == 2:
        if int(columnScope) == 1:
            return ['kindle_id', 'ASIN', 'Reviewer ID', 'Overall', 'Summary', 'Review Time']
        else:
            return ['ASIN', 'Reviewer ID', 'Overall', 'Review Time']

def toDict(mysqlResult, columns):
    myDictionaries = dict()

    for row in mysqlResult:
        myDictionary = dict()
        for col_index in range(len(row)):

            myDictionary[columns[col_index]] = row[col_index]

        myDictionaries[myDictionary[columns[0]]] = myDictionary

    return myDictionaries

def find(scope=1, debug=False, columns=['*'], customization=['']):
    # Control variables used to switch between sandbox and prod
    table = ''
    myDB = db

    # Control variable used to prepare de query
    col_length = len(columns)
    custom_length = len(customization)

    # Switching between tables
    if debug:
        table = 'MyUsers'
    elif int(scope) == 1:
        table = 'amz200k'
    elif int(scope) == 2:
        table = 'amzkindle'

    # Preparing the query for dynamic column calling
    query = f"SELECT "

    # Adding the columns needed to prepare the query
    for col_index in range(col_length):

        # For debugging purposes only
        if not debug:
            query += "`"

        query += f"{str(columns[col_index])}"

        # For debuggin purposes only
        if not debug:
            query += "`"

        # Will only add a comma at the end if we are not last element of the column list
        if col_length - (col_index + 1) > 0:
            query += ","

    # Adding From {tablename} clause
    query += f" FROM `{str(table)}`"

    # Adding customization clauses - limit, group by, order by,
    for index in range(custom_length):
        query += f" {str(customization[index])}"

    # Adding closing semicolon to end query
    query += ";"

    # Starting MySQL 5.7 connection
    try:

        # Terniary Operator
        mycursor = _connection_prod.cursor() if debug else _connection_debug.cursor()
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        mycursor.close()
        print(type(myresult))
        print(type(myresult[0]))
        print(myresult)

        return toDict(mysqlResult=myresult, columns=columns)
        # return str(myresult)

    except mysql.connector.errors.ProgrammingError:
        print(query)
        raise
    except mysql.connector.errors.DatabaseError:
        print(query)
        raise
    except mysql.connector.errors.DataError:
        print(query)
        raise


def exampleTable(scope=1):
    return find(scope=scope, debug=False, columns=getCol(scope=scope, columnScope=1), customization=['LIMIT 5'])


def createStudent(firstName, lastName):
    mycursor = _connection_prod.cursor()
    mycursor.execute(f"Insert INTO myusers (firstname, lastname) values ('{str(firstName)}','{str(lastName)}');")
    _connection_prod.commit()

    return "Finished"



