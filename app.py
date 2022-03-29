from flask import Flask, jsonify, request

app = Flask(__name__)

numbers = [
    {
        'id': 1,
        'contact': '7567528552',
        'name': 'Yash',
        'done': False
    },
    {
        'id': 2,
        'contact': '9374989826',
        'name': 'Pratiyush',
        'done': False,
    },
    {
        'id': 3,
        'contact': '8923773667',
        'name': 'Varun',
        'done': False,
    },
]

@app.route("/add-data", methods = ['POST'])

def add_number():
    if not request.jason:
        return jsonify({
            "status": 'error',
            'message': 'please provide the data',
        }, 
        400
        )
    number= {
        "id": numbers[-1]['id']+1,
        'title': request.json['title'],
        'contact': request.json.get('contact', ""),
        'done': False
    }
    numbers.append(number)
    return jsonify({
        'status': 'success',
        'message': 'number added successfully!',
    })

@app.route("/get-data")

def get_number():
    return jsonify({
        "data": numbers
    })

if(__name__ == '__main__'):
    app.run(debug= True)