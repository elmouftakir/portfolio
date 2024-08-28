
```python
        # User signup data payload
        "password": "password"
        }

        # Send POST request to '/auth/signup' endpoint with signup data
        response = self.client.post('/auth/signup', json=data)

        # Query the database to find the user with the specified email
        user = User.query.filter_by(email="testuser@company.com").first()

        # Assert that the user was successfully created with the correct username
        assert user.username == "testuser"

        # Assert that the signup request was successful and returned a 201 status code
        assert response.status_code == 201


    def test_login(self):
        # User login data payload
        data = {
            "email": "testuser@gmail.com",
            "password": "password"
        }

        # Send POST request to '/auth/login' endpoint with login data
        response = self.client.post('/auth/login', json=data)

        # Assert that the login request failed and returned a 400 status code
        assert response.status_code == 400
