from flask import Flask, jsonify, request

app = Flask(__name__)
stores=[
    {
        'name':'My Store',
        'items':[
            {
                'name': 'My Item',
                'Price': 200
            }
        ]
    }
]
#as server perspective
#post use to recieve date
#get use to send data

#post /store data: (name)
@app.route("/store", methods= ["Post"])
def create_store():
    request_data= request.get_json()

#get/store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    pass


#get store
@app.route("/store")
def get_stores():
    return jsonify({'stores':stores})


#post /store/<string:name>/item
@app.route("/store/<string:name>/item", methods= ["Post"])
def create_item_in_store():
    pass

#get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass

app.run(port=5000)