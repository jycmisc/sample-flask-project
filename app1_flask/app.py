from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
    {
        "name": "Main Store",
        "items": [
            {
                "name": "Item 1",
                "price": 15.99
            },
            {
                "name": "Item 2",
                "price": 12.99
            },
            {
                "name": "Item 3",
                "price": 11.99
            }
        ]
    },
    {
        "name": "New York Store",
        "items": [
            {
                "name": "Item 1",
                "price": 120.99
            },
            {
                "name": "Item 2",
                "price": 223.99
            },
            {
                "name": "Item 3",
                "price": 621.99
            }
        ]
    }
]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

def index():
    return 'Hello, World!'

# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})

# GET /store
@app.route('/store', methods=['GET'])
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5000)