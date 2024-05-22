from flask import Flask, jsonify


app = Flask(__name__)

# Sample data for users
users = [
    {'id': 1, 'name': 'Alice', 'age': 30},
    {'id': 2, 'name': 'Bob', 'age': 25},
    {'id': 3, 'name': 'Charlie', 'age': 35},
]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})


port = 5000
app.run(debug=True, host='127.0.0.1', port=port)