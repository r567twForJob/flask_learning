from flask import Flask, request
from db import store, items

app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = "/uploads"


@app.get('/')
def HelloWorld():
    return {"stores": stores}


@app.post('/')
def addStore():
    data = request.get_json()
    newstore = {"name": data['name'], "items": []}
    stores.append(newstore)
    return newstore, 201


@app.post('/store/<string:name>/items')
def addStoreItems(name):
    data = request.get_json()
    item = {"name": data['name']}

    for store in stores:
        if store['name'] == name:
            store['items'].append(item)
            return store
    return {"message": "this store not found"}, 404


@app.route("/upload", methods=["post"])
def upload():
    image = request.files['image']
    image.save("./{}".format(image.filename))
    return {"message": "image upload"}, 201
