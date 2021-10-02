import flask
from flask import jsonify
from flask import request, make_response


#from sql import execute_connection
#from sql import execute_query
#from sql import execute_read_query


#setting the application name
app = flask.Flask(__name__) #Sets up the application
app. config["DEBUG"] = True #Allows errors on browser












@app.route('/', methods=['GET']) #Contact the endpoint
def home():
    return "Welcome to Homework"

@app.route('/api/cart', methods=['GET'])


def cart():
    return jsonify(items)     


@app.route('/api/cart', methods=['GET'])
def api_id():
    if 'item' in request.args:
        id = int(request.args['item'])
    else:
        return "NO SUCH ITEM"

    results = []
    for cart in carts:
        if cart['item'] == item:
            results.append(cart)



app.run()