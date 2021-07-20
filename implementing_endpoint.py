from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores=[
    {
        'name':'My Wonderful Store',
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


# @app.route('/')
# def home():
#     return render_template('index.html')
#post /store data: (name)
@app.route("/store", methods= ["POST"])
def create_store():
    request_data= request.get_json()
    new_store= {
        'name':request_data['name'],
        'item':[]
    }
    stores.append(new_store)
    return jsonify(new_store)

#get/store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    #iterate over stores
    for store in stores:
    #if the store name matches, returns the store name
        if store['name']== name:
            return jsonify(store)
    #if none match return the error message
    return jsonify({'message': 'store not find'})

#get store
@app.route("/store")
def get_stores():
    return jsonify({'stores':stores})


#post /store/<string:name>/item
@app.route("/store/<string:name>/item", methods= ["Post"])
def create_item_in_store():
    request_data= request.get_json()
    for store in stores:
        if store['name']== name:
            new_item={
                'name':request_data['name'],'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
        return jsonify({'message':'store not found'})
        
#get /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name']== name:
            return jsonify({'items': stores['items']})
    return jsonify({'message':'store not found'})


app.run(port=5000)