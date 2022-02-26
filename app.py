from flask import Flask, render_template, \
    make_response, send_from_directory, request, redirect, json, jsonify

app = Flask(__name__)


@app.route('/test')
def index():
    return render_template("index_test.html", title="Home", link="/form")


@app.route('/')
def test():
    return render_template("index.html", title="test")


@app.route("/form", methods=['GET'])
def form():
    table = request.args.get('table', " ")
    size = request.args.get('size', " ")
    reserv = {"Table": table, "Size": size}

    return jsonify(reserv)#render_template("form.html", title="Prenotazione")


""""@app.route('/form', methods=['POST'])
def reserveUp():
    # read the posted values from the UI
    _name = request.form['inputName']
    _surname = request.form['inputName']
    _cell = request.form['inputCell']
    _email = request.form['inputEmail']
    _person = request.form['inputPerson']

    # validate the received values
    if _name and _surname and _cell and _email and _person:
        return redirect('/index_test.html')
    else:
        return json.dumps({'html': '<span>Ente the required fields</span>'})
"""

@app.route('/sw.js')
def sw():
    response = make_response(
        send_from_directory('static', 'sw.js'))
    response.headers['Content-Type'] = 'application/javascript'
    return response


if __name__ == '__main__':
    app.run(debug=True)
