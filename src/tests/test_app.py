import json
import pytest
import coverage
from app.app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_user(client):
    new_user = {
        'username': 'testuser',
        'email': 'test@example.com',
        'phone_number': '1234567890',
        'city': 'Test City',
        'designation': 'Tester'
    }
    response = client.post('/users', json=new_user)
    assert response.status_code == 200  # Replace with the expected status code
    # Add more assertions based on your application's logic

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200  # Replace with the expected status code
    # Add more assertions based on your application's logic

# def test_get_user(client):
#     response = client.get('/users/1')
#     assert response.status_code == 200  # Replace with the expected status code
#     # Add more assertions based on your application's logic

def test_update_user(client):
    updated_user = {
        'username': 'updateduser',
        'email': 'updated@example.com',
        'phone_number': '0987654321',
        'city': 'Updated City',
        'designation': 'Updated Tester'
    }
    response = client.put('/users/1', json=updated_user)
    assert response.status_code == 200  # Replace with the expected status code
    # Add more assertions based on your application's logic

# def test_delete_user(client):
#     response = client.delete('/users/1')
#     assert response.status_code == 200  # Replace with the expected status code
#     # Add more assertions based on your application's logic


# # test_app.py

# import pytest
# from app.app import create_app

# @pytest.fixture
# def app():
#     app = create_app()
#     yield app

# @pytest.fixture
# def client(app):
#     return app.test_client()

# def test_create_user(client):
#     response = client.post('/users', json={'username': 'testuser', 'email': 'test@example.com'})
#     assert response.status_code == 200  # Replace with the expected status code
#     # Add more assertions based on your application's logic

# def test_get_users(client):
#     response = client.get('/users')
#     assert response.status_code == 200  # Replace with the expected status code
#     # Add more assertions based on your application's logic

# def test_get_user(client):
#     # Assuming there's a user with ID 1
#     response = client.get('/users/1')
#     assert response.status_code == 200  # Replace with the expected status code
#     # Add more assertions based on your application's logic

# def test_update_user(client):
#     # Assuming there's a user with ID 1
#     response = client.put('/users/1', json={'username': 'updateduser', 'email': 'updated@example.com'})
#     assert response.status_code == 200  # Replace with the expected status code
#     # Add more assertions based on your application's logic

# def test_delete_user(client):
#     # Assuming there's a user with ID 1
#     response = client.delete('/users/1')
#     assert response.status_code == 200  # Replace with the expected status code
#     # Add more assertions based on your application's logic

# # import json
# # import pytest
# # #from app import create_app
# # from app.app import create_app

# # # Assuming your app is created with a create_app function
# # app = create_app()

# # @pytest.fixture
# # def client():
# #     app.config['TESTING'] = True
# #     client = app.test_client()

# #     # Create a test database and tables
# #     with app.app_context():
# #         cursor = app.mysql.cursor(dictionary=True)  # Use app.mysql.cursor() instead of mysql.cursor()
# #         cursor.execute("CREATE DATABASE IF NOT EXISTS test_database")
# #         cursor.execute("USE test_database")
# #         cursor.execute("""
# #             CREATE TABLE IF NOT EXISTS users (
# #                 id INT AUTO_INCREMENT PRIMARY KEY,
# #                 username VARCHAR(50) NOT NULL,
# #                 email VARCHAR(100) NOT NULL,
# #                 phone_number VARCHAR(15),
# #                 city VARCHAR(50),
# #                 designation VARCHAR(50)
# #             )
# #         """)
        
# #         # Create a test user with ID 1
# #         cursor.execute("INSERT INTO users (id, username, email) VALUES (1, 'testuser', 'test@example.com')")
        
# #         app.mysql.commit()

# #     yield client

# #     # Drop the test database after testing
# #     with app.app_context():
# #         cursor = app.mysql.cursor(dictionary=True)  # Use app.mysql.cursor() instead of mysql.cursor()
# #         cursor.execute("DROP DATABASE IF EXISTS test_database")
# #         app.mysql.commit()

# # def test_create_user(client):
# #     response = client.post('/users', json={'username': 'testuser', 'email': 'test@example.com'})
# #     assert response.status_code == 200
# #     assert json.loads(response.data)['message'] == 'User created successfully'

# # def test_get_users(client):
# #     response = client.get('/users')
# #     assert response.status_code == 200
# #     assert 'users' in json.loads(response.data)

# # def test_get_user(client):
# #     # Assume there's a user with ID 1
# #     response = client.get('/users/1')
# #     assert response.status_code == 200
# #     assert 'user' in json.loads(response.data)

# # def test_update_user(client):
# #     # Assume there's a user with ID 1
# #     response = client.put('/users/1', json={'username': 'updateduser', 'email': 'updated@example.com'})
# #     assert response.status_code == 200
# #     assert json.loads(response.data)['message'] == 'User updated successfully'

# # def test_delete_user(client):
# #     # Assume there's a user with ID 1
# #     response = client.delete('/users/1')
# #     assert response.status_code == 200
# #     assert json.loads(response.data)['message'] == 'User deleted successfully'
