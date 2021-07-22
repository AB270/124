from flask import Flask,jsonify, request

app = Flask(__name__)

details = [
    {
        'contact': 999999999,
        'name': u'ABC',
        'done': False,
        'id': 1
    },
    {
        'contact': 999999998,
        'name': u'ABC2',
        'done': False,
        'id': 2
    }
]


@app.route("/add-data", methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    details = {
        'id': details[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    tasks.append(details)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : details
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)
