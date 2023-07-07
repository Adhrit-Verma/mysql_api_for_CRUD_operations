from flask import Flask, request, jsonify
import mysql.connector
import db_creator

app = Flask(__name__)
db=db_creator()

# MySQL Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'users'
}

# Error Response Helper Function
def create_error_response(message, status_code):
    response = jsonify({'error': message})
    response.status_code = status_code
    return response

# GET /users - Retrieve a list of all users
@app.route('/users', methods=['GET'])
def get_all_users():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({'users': users})
    except Exception as e:
        return create_error_response(str(e), 500)

# GET /users/{id} - Retrieve details of a specific user
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = %s', (id,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            return jsonify({'user': user})
        else:
            return create_error_response('User not found', 404)
    except Exception as e:
        return create_error_response(str(e), 500)

# POST /users - Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    try:
        user_name = request.json['user_name']
        password = request.json['password']
        phone = request.json['phone']
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (user_name, password, phone) VALUES (%s, %s, %s)', (user_name, password, phone))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'User created successfully'})
    except Exception as e:
        return create_error_response(str(e), 500)

# PUT /users/{id} - Update details of a specific user
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user_name = request.json['user_name']
        password = request.json['password']
        phone = request.json['phone']
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET user_name = %s, password = %s, phone = %s WHERE id = %s', (user_name, password, phone, id))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'User updated successfully'})
    except Exception as e:
        return create_error_response(str(e), 500)

# DELETE /users/{id} - Delete a specific user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM users WHERE id = %s', (id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'message': 'User deleted successfully'})
    except Exception as e:
        return create_error_response(str(e), 500)

if __name__ == '__main__':
    app.run(debug=True)
