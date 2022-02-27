from bson import ObjectId
from flask import Flask, render_template, make_response, send_from_directory, request, redirect, jsonify
from database import posts


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

    items = posts.find()
    post_list = []
    for item in items:
        item["_id"] = str(item["_id"])
        post_list.append(item)

    result = {"posts": post_list}
    return jsonify(result)



@app.route("/formdate", methods=['POST'])
def formdate():


    post = {
        "name": request.form.get('name', ''),
        "surname": request.form.get('surname', ' ')
    }
    result = posts.insert_one(post)
    return jsonify({"post": str(result.inserted_id)})




@app.route("/conferma")
def conferma():
    return render_template("Conferma.html")




@app.route('/sw.js')
def sw():
    response = make_response(
        send_from_directory('static', 'sw.js'))
    response.headers['Content-Type'] = 'application/javascript'
    return response





if __name__ == '__main__':
    app.run(debug=True)
