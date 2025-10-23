# Put and Delete - HTTP Verbs
# Working With API's -- JSON

from flask import Flask,jsonify, request

app = Flask(__name__)


## Initial Data in my to do list

items = [
    {"id": 1,"name":"Item 1","description":"This is item 1"},
    {"id": 2,"name":"Item 2","description":"This is item 2"}
]

@app.route("/") # By default, the method will be GET
def home():
    return "Welcome To the Sample TODO List App"

# Retrieve all the items
# Jsonify returns the items in the form of JSON
@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

# Retrieve a specific item by ID
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id),None)
    if item == None:
        return jsonify({"error" : "Item Not Found"})
    return jsonify(item)


# Post : Create a new task - API
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error" : "Item Not Found"})
    new_item = {
        "id" : items[-1]["id"] + 1 if items else 1,
        "name" : request.json['name'],
        "description" : request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item)


#Put : Update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id),None)
    if item == None:
        return jsonify({"error" : "Item Not Found"})
    item['name'] = request.json.get('name',item['name'])
    item['description'] = request.json.get('description',item['description'])
    return jsonify(item)

#Delete
@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_item(item_id):
    '''
        Python treats variables differently inside functions:

        1. If you only read a global variable → you can access it directly.
        2. If you try to modify a global variable (like reassign it), Python automatically assumes you're 
           creating a new local variable, unless you explicitly declare it as global.
    '''
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result" : "Item deleted"})

if __name__ == '__main__':
    app.run(debug=True)