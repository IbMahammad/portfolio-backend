# **Portfolio Backend API**

This is the backend for a personal portfolio application built using Django and Django REST Framework. The API allows for managing various portfolio-related information such as projects, skills, achievements, and contact messages.

### **Features**
- CRUD functionality for **Projects**, **Skills**, **Achievements**
- Contact form to send messages to the portfolio owner
- JWT-based authentication (for future enhancements)

### **Installation**
1. Make sure you have Python 3.x and pip installed.
2.     ```sh
    cd portfolio_backend
    ```

3. Install the required dependencies by running the following command:

    ```sh
    pip install -r requirements.txt
    ```

### **Database Setup**
Before running the project, you need to apply migrations to set up the database. Run these commands:

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

### **Running the Server**
After setting up the database, you can start the Django development server with this command:

    ```sh
    python manage.py runserver
    ```

Once the server is running, you can access it at `http://127.0.0.1:8000/`.

### **API Endpoints**

- **GET** `/api/projects/`: Retrieve all projects in the portfolio.
- **POST** `/api/projects/`: Create a new project in the portfolio. The request body should include:
    - `title`: Project title.
    - `description`: Project description.
    - `link`: Project link (optional).

- **GET** `/api/skills/`: Retrieve all skills.
- **POST** `/api/skills/`: Add a new skill to the portfolio.

- **GET** `/api/achievements/`: Retrieve all achievements.
- **POST** `/api/achievements/`: Add a new achievement.

- **GET** `/api/contact-messages/`: Retrieve all messages from the contact form.
- **POST** `/api/contact-messages/`: Send a message via the contact form. The request body should include:
    - `email`: Sender’s email address.
    - `subject`: Message subject.
    - `message`: Message content.

### **Project Setup**

1. **Email Configuration**: The backend sends messages using Gmail's SMTP. Make sure to configure your email credentials in the `settings.py` file.
   
   - Replace `EMAIL_HOST_USER` with your Gmail address.
   - Use an **App Password** if you have 2FA enabled on your Gmail account. Set it in `EMAIL_HOST_PASSWORD`.

2. **JWT Authentication** (Future): JWT-based user authentication is planned for user login. Currently, this project supports basic CRUD operations for portfolio information.

### **Security Notes**
- Ensure that sensitive data such as your **Gmail app password** is securely managed and **not hardcoded** into the repository.
- Always use **HTTPS** in production to protect the integrity of user data.

### **Technologies Used**
- **Django**: Web framework for building the API.
- **Django REST Framework**: To create RESTful API endpoints.
- **SQLite**: Default database for development.
- **Django's email backend**: For sending contact form submissions.
- **Swagger**: API documentation provided via `drf_yasg`.

### **Notes**
- Make sure to configure your database settings and other environment variables in `settings.py`.
- The portfolio's `projects`, `skills`, and `achievements` can be easily updated using the provided API endpoints.


