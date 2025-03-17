from flask import Flask,jsonify,request

app = Flask(__name__)

items = [
    {"id":1,"name":"item1","price":100},
    {"id":2,"name":"item2","price":200},
    {"id":3,"name":"item3","price":300}
]

## get req

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:id>',methods=['GET'])
def get_item(id):
    item = next(filter(lambda x:x['id']==id,items),None)
    return jsonify(item)

### post req

@app.route('/items',methods=['POST'])
def add_item():
    if not request.json or not 'name' in request.json:
        return "Invalid request",400
    item = {
        "id":items[-1]['id']+1,
        "name":request.json['name'],
        "price":request.json.get('price',0)
    }
    items.append(item)
    return jsonify(item)


### put req 

@app.route('/items/<int:id>',methods=['PUT'])
def update_item(id):
    item = next(filter(lambda x:x['id']==id,items),None)
    if item:
        item['name'] = request.json.get('name',item['name'])
        item['price'] = request.json.get('price',item['price'])
    return jsonify(item)

##delete req

@app.route('/items/<int:id>',methods=['DELETE'])
def delete_item(id):
    item = next(filter(lambda x:x['id']==id,items),None)
    if item:
        items.remove(item)
    return jsonify(items)




if __name__ == '__main__':
    app.run(debug=True)