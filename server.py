from flask import Flask, request, jsonify

app = Flask(__name__)

employees = [] 

# Greeting
@app.route("/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

# Create Employee
@app.route('/employee', methods=['POST'])
def create_employee():
    try:
        data = request.json
        if 'name' in data and 'city' in data:
            employee_id = str(len(employees) + 1)
            data['employeeId'] = employee_id
            employees.append(data)
            return jsonify({"employeeId": employee_id}), 201
        else:
            return jsonify({"message": "Invalid data"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500

# Get all Employee details
@app.route('/employees/all', methods=['GET'])
def get_all_employees():
    return jsonify(employees)

# Get Employee details
@app.route('/employee/<employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = next((e for e in employees if e['employeeId'] == employee_id), None)
    if employee:
        return jsonify(employee)
    return jsonify({"message": f"Employee with {employee_id} was not found"}), 404

# Update Employee
@app.route('/employee/<employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.json
    employee = next((e for e in employees if e['employeeId'] == employee_id), None)
    if employee:
        employee.update(data)
        return jsonify(employee), 201
    return jsonify({"message": f"Employee with {employee_id} was not found"}), 404

# Delete Employee
@app.route('/employee/<employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = next((e for e in employees if e['employeeId'] == employee_id), None)
    if employee:
        employees.remove(employee)
        return jsonify(employee), 200
    return jsonify({"message": f"Employee with {employee_id} was not found"}), 404

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')