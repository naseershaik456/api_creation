from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)


# Store admission data in-memory (not recommended for production)
admission_data = []

# API endpoint to submit admission form
@app.route('/api/admission', methods=['POST'])
def submit_admission_form():
    data = request.json
    admission_data.append(data)
    
    return jsonify({'message': 'Admission form submitted successfully'})

# API endpoint to retrieve all admission data
@app.route('/api/admissions', methods=['GET'])
def get_admission_data():
    if request.method == "GET":
        return jsonify(admission_data)

if __name__ == '__main__':
    app.run(debug=True)
