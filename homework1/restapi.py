import flask
from flask import jsonify
from flask import request, make_response
from sql import execute_connection
from sql import execute_query
from sql import execute_read_query


#setting the application name
app = flask.Flask(__name__) #Sets up the application
app. confic["DEBUG"] = True #Allows errors on browser












@app.route('/', methods=['GET']) #Contact the endpoint
def home():
    return "Welcome to Homework 1"




app.run()