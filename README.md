# Django Machine Test Project

This project is a Django REST API application that allows users to:

1. Sign up (User Registration).
2. Log in and generate an authentication token.
3. Register clients.
4. Fetch client information.
5. Edit/Delete client information.
6. Add new projects for a client and assign users to those projects.
7. Retrieve projects assigned to logged-in users.

**NOTE**: Scroll to end for my images.

## Prerequisites

- Python 3.7 or higher
- Django 3.x or higher
- Django REST Framework
- MySQL
- Git (optional, for version control)

## Project Setup

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Database Setup

#### Option A: Using MySQL

1. Install MySQL on your system.
2. Create a database and user in MySQL:

   ```sql
   CREATE DATABASE your_database_name;
   CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON your_database_name.* TO 'your_username'@'localhost';
   FLUSH PRIVILEGES;
   ```

3. Configure Django to use MySQL in `settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_username',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

#### Option B: Using SQLite (For Simplicity)

If MySQL is not installed, use SQLite by default. No additional configuration is required as Django uses SQLite by default for local development.

### 5. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional)

To access the Django admin and manage users and clients:

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Endpoints

#### 1. **User Signup**

- **Endpoint**: `/signup/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password",
    "password2": "confirm_password"
  }
  ```

#### 2. **User Login and Token Generation**

- **Endpoint**: `/login/`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```
- **Response**:
  ```json
  {
    "token": "generated_token"
  }
  ```

#### 3. **Register a Client**

- **Endpoint**: `/clients/`
- **Method**: `POST`
- **Headers**: `Authorization: Token <your_token>`
- **Request Body**:
  ```json
  {
    "client_name": "Client Name"
  }
  ```

#### 4. **Fetch Clients Info**

- **Endpoint**: `/clients/`
- **Method**: `GET`
- **Headers**: `Authorization: Token <your_token>`

#### 5. **Edit/Delete Client Info**

- **Endpoint**: `/clients/:id/`
- **Method**: `PUT`, `PATCH`, or `DELETE`
- **Headers**: `Authorization: Token <your_token>`

#### 6. **Add New Projects for a Client and Assign Users to those Projects**

- **Endpoint**: `/clients/:id/projects/`
- **Method**: `POST`
- **Headers**: `Authorization: Token <your_token>`
- **Request Body**:
  ```json
  {
    "project_name": "Project A",
    "users": [
      {
        "id": 1,
        "name": "User1"
      }
    ]
  }
  ```

#### 7. **Retrieve Assigned Projects to Logged-in Users**

- **Endpoint**: `/projects/`
- **Method**: `GET`
- **Headers**: `Authorization: Token <your_token>`

### 9. Testing the API

You can use tools like [Postman](https://www.postman.com/) or [cURL](https://curl.se/) or [Hoppscotch](https://hoppscotch.io/) to test the API endpoints.

### 10. Deactivating the Virtual Environment

After you're done, deactivate the virtual environment:

```bash
deactivate
```

![Alt text for image](relative/path/to/image)

# Example:

![Create a new Client](images/Create%20a%20new%20Client.png)
![Client List](images/List%20all%20client.png)
![Project Assignment](images/Create%20a%20new%20Project%20for%20client.png)
![Project List](images/List%20Projects%20for%20logged%20in%20user.png)
