from flask import Flask, request, jsonify

app = Flask(__name__)

# Load Student Details API
@app.route('/students', methods=['GET'])
def get_students(students_data=None):
    # Read the file and retrieve all student details
    # Apply pagination based on the provided page number and page size
    page_number = int(request.args.get('page', 1))
    page_size = int(request.args.get('size', 10))
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size

    # Assuming students_data is a list of dictionaries containing student details
    paginated_students = students_data[start_index:end_index]

    return jsonify(paginated_students)

# Server-side Filtering API
@app.route('/students/filter', methods=['POST'])
def filter_students():
    filter_criteria = request.json  # Assuming filter criteria are sent in the request body

    filtered_students = []
    # Iterate over students_data and apply filters based on the criteria
    for student in students_data:
        # Apply filtering based on the provided filter criteria
        if student['id'] == filter_criteria.get('id'):
            filtered_students.append(student)
        # Add other filtering conditions for different columns (e.g., name, total marks) as per requirements

    return jsonify(filtered_students)

if __name__ == '__main__':
    app.run()
