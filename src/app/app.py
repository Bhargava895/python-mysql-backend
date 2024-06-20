from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS 

def create_app():
    app = Flask(__name__)
    CORS(app) 
    app.config['MYSQL_HOST'] = '3.93.247.5'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'users'

    # Connect to the database
    app.mysql = mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

    # Create a cursor
    app.cursor = app.mysql.cursor()

    # Create a users table if it doesn't exist
    app.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL,
            phone_number VARCHAR(15),
            city VARCHAR(50),
            designation VARCHAR(50)
        )
    """)
    app.mysql.commit()

    # Define CRUD operations
    @app.route('/users', methods=['GET'])
    def get_users():
        app.cursor.execute("SELECT * FROM users")
        users = app.cursor.fetchall()
        user_list = []
        for user in users:
            user_dict = {
                'id': user[0],
                'username': user[1],
                'email': user[2],
                'phone_number': user[3],
                'city': user[4],
                'designation': user[5]
            }
            user_list.append(user_dict)
        return jsonify({'users': user_list})

    @app.route('/users', methods=['POST'])
    def create_user():
        data = request.get_json()
        username = data['username']
        email = data['email']
        phone_number = data.get('phone_number', None)
        city = data.get('city', None)
        designation = data.get('designation', None)
        
        app.cursor.execute("""
            INSERT INTO users (username, email, phone_number, city, designation)
            VALUES (%s, %s, %s, %s, %s)
        """, (username, email, phone_number, city, designation))
        app.mysql.commit()

        return jsonify({'message': 'User created successfully'})

    @app.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        app.cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = app.cursor.fetchone()
        if user:
            user_dict = {
                'id': user[0],
                'username': user[1],
                'email': user[2],
                'phone_number': user[3],
                'city': user[4],
                'designation': user[5]
            }
            return jsonify({'user': user_dict})
        else:
            return jsonify({'message': 'User not found'}), 404

    @app.route('/users/<int:user_id>', methods=['PUT'])
    def update_user(user_id):
        data = request.get_json()
        new_username = data['username']
        new_email = data['email']
        new_phone_number = data.get('phone_number', None)
        new_city = data.get('city', None)
        new_designation = data.get('designation', None)

        app.cursor.execute("""
            UPDATE users 
            SET username = %s, email = %s, phone_number = %s, city = %s, designation = %s
            WHERE id = %s
        """, (new_username, new_email, new_phone_number, new_city, new_designation, user_id))
        app.mysql.commit()

        return jsonify({'message': 'User updated successfully'})

    @app.route('/users/<int:user_id>', methods=['DELETE'])
    def delete_user(user_id):
        app.cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        app.mysql.commit()

        return jsonify({'message': 'User deleted successfully'})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
