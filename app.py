from bson import ObjectId
from flask import Flask, render_template, make_response, send_from_directory, request, redirect, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def test():
    return render_template("index.html")


@app.route("/form", methods=['GET'])
def form():
    table = request.args.get('table', " ")
    size = request.args.get('size', " ")
    reserv = {"Table": table, "Size": size}
    return jsonify(reserv)


@app.route("/formdates", methods=['GET'])
def list_posts():
    # Crea un’istanza del client
    client = MongoClient("mongodb://localhost:27017/")

    # Accede ad un database (se non presente, allora è creato)
    db = client["reserve"]

    # Accedo ad una collezione (se non presente, allora è creata)
    posts = db["posts"]

    #items = posts.find({},{"_id":0})
    items = posts.find()
    post_list = []
    for item in items:
        item["_id"] = str(item["_id"])
        post_list.append(item)

    result = {"posts": post_list}
    return jsonify(result)


@app.route("/formdate/<id>", methods=['GET'])
def list_post_by_id(id):
    # Crea un’istanza del client
    client = MongoClient("mongodb://localhost:27017/")

    # Accede ad un database (se non presente, allora è creato)
    db = client["reserve"]

    # Accedo ad una collezione (se non presente, allora è creata)
    posts = db["posts"]

    item = posts.find_one({"_id": ObjectId(id)})
    item["_id"] = str(item["_id"])
    result = {"post": item}
    return jsonify(result)


@app.route("/formdate", methods=['POST'])
def formdate():
    # crea istanza client
    client = MongoClient("mongodb://localhost:27017/")

    # Accede ad un database e lo crea
    db = client["reserve"]

    # accedo a una collezione
    posts = db["posts"]
    post = {
        "name": request.form.get('name', ''),
        "surname": request.form.get('surname', ' ')
    }
    result = posts.insert_one(post)
    return jsonify({"post": str(result.inserted_id)})


@app.route('/sw.js')
def sw():
    response = make_response(
        send_from_directory('static', 'sw.js'))
    response.headers['Content-Type'] = 'application/javascript'
    return response


if __name__ == '__main__':
    app.run(debug=True)
