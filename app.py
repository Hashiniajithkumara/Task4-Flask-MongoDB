from flask import Flask, render_template, request, jsonify
from db import collection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()

        required_fields = ['firstName', 'lastName', 'email', 'title', 'description', 'dueDate']

        if not all(field in data and data[field] for field in required_fields):
            return jsonify({"message": "Please fill in all fields."}), 400

        result = collection.insert_one(data)

        return jsonify({
            "message": "Task submitted successfully!",
            "id": str(result.inserted_id)
        })

    except Exception as e:
        print("Error:", e)
        return jsonify({"message": "Something went wrong"}), 500


if __name__ == '__main__':
    app.run(debug=True)