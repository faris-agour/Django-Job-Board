# Django-Job-Board

Django-Job-Board is an advanced job board web application that uses the Django framework and a MySQL database. It is designed to be efficient, secure, and user-friendly, catering to both job seekers and employers.

## Features

- **Django Framework with MySQL**: Built with Django and MySQL for a reliable and scalable job board solution.
- **Job Search and Filtering**: Job listings are easy to browse with advanced filters for a custom search experience.
- **Pagination**: Pagination is implemented for efficient navigation and quick access to various job opportunities.
- **Secure User Authentication**: Features secure login and signup functionalities to protect user data.
- **Contact Form with Email Integration**: Includes a contact form with email integration for seamless communication between users and administrators.
- **Responsive Design**: The web app is designed to be responsive, providing a consistent experience across different devices.


## Screenshots

<!-- Add screenshots or images showcasing the project's interface -->
<img src="https://github.com/fares-agour/Django-Job-Board/assets/116801554/6f56a4b2-b053-4feb-8b0b-e28af453acaa" width="400">
<img src="https://github.com/fares-agour/Django-Job-Board/assets/116801554/2e00a511-beee-4f53-a508-471abbfe018a" width="400">
<img src="https://github.com/fares-agour/Django-Job-Board/assets/116801554/81f0e77d-74f6-4162-9d4c-7441df18b8cc" width="400">
<img src="https://github.com/fares-agour/Django-Job-Board/assets/116801554/1979d622-830f-4bad-a2a1-52c30671ac18" width="400">




## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Django-Job-Board.git
   cd django-job-board

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`
    
3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    
4. **Set up the database:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser

6. **Run the development server:**
    ```bash
    python manage.py runserver
