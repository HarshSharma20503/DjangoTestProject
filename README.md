# Test Django Project

## Steps to create a django project

### Step 1: Set up Your Python Virtual Environment

1. Navigate to your project directory (where you want to create the project):

    ```bash
    mkdir my_django_project
    cd my_django_project
    ```

2. Create a virtual environment (Python 3 must be installed on your system):

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

    - On Windows:

      ```bash
      .\venv\Scripts\activate
      ```

### Step 2: Install Django

Install Django in your virtual environment:

```bash
pip install django
```

### Step 3: Create Django Project and App

1. Create a new Django project

    ```bash
    django-admin startproject mywebsite .
    ```

2. Create an app called main:

    ```bash
    python manage.py startapp main
    ```

3. Register the main app in your project’s settings:

    - Open mywebsite/settings.py and add 'main' to the INSTALLED_APPS list.

4. Set up the database by running the initial migrations:

    ```bash
    python manage.py migrate
    ```

### Step 4: Create Model

1. Define the model in main/models.py

    ```python
    from django.db import models

    class Message(models.Model):
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"Message {self.id}"
    ```

2. Create the database migration for the model:

    ```bash
    python manage.py makemigrations main
    ```

3. Apply the migration to create the table in the database:

    ```bash
    python manage.py migrate
    ```

### Step 5: Set up Views and URL Routing

1. Define views for home and form pages in main/views.py

    ```python
    from django.shortcuts import render, redirect
    from .models import Message

    def home(request):
        messages = Message.objects.all().order_by('-created_at')[:1]  # Fetch the latest message
        return render(request, 'home.html', {'messages': messages})

    def form_view(request):
        if request.method == 'POST':
            content = request.POST.get('content')
            Message.objects.create(content=content)
            return redirect('home')
        return render(request, 'form.html')
    ```

2. Set up URLs in main/urls.py:

    - Create the urls.py if not exists.

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='home'),
        path('form/', views.form_view, name='form'),
    ]
    ```

3. Link main/urls.py to the project's main urls.py:

    - in mywebsite/urls.py, add an import and include the main app's URL

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```

### Step 6: Create Templates and Static Files

1. Create a templates folder within the main app, and inside it create home.html and form.html

2. Create a static folder in the main app directory for CSS and Javascript, and images.

3. Set up Bootstrap and custom CSS.

    - Add a style.css file inside the main/static/main/css/ for any additional styling.

4. Add home.html Code

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        {% load static %}
        <!-- Load the static template tag library -->

        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Home</title>
        <link
        rel="stylesheet"
        href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
        />
        <link rel="stylesheet" href="{% static 'css/style.css' %}" />
        <!-- Correct static usage -->
    </head>
    <body>
        <!-- Section 1: Landing Page -->
        <section
        class="landing text-center text-white d-flex align-items-center justify-content-center text-primary"
        >
        <h1>Welcome to My Website</h1>
        </section>

        <!-- Section 2: Cards -->
        <section class="container mt-5">
        <div class="row">
            <div class="col-md-6 mb-4">
            <div class="card">
                <div class="card-body">
                <h5 class="card-title">Card Title</h5>
                <p class="card-text">This is card number.</p>
                </div>
            </div>
            </div>
        </div>
        </section>

        <!-- Section 3: Message Section -->
        <section class="container mt-5">
        <h2>Latest Message</h2>
        {% for message in messages %}
        <p>{{ message.content }}</p>
        {% empty %}
        <p>No messages available.</p>
        {% endfor %}
        </section>
    </body>
    </html>

    ```

5. Add form.html Code

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Submit Message</title>
        <link
        rel="stylesheet"
        href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"
        />
    </head>
    <body>
        <div class="container mt-5">
        <h2>Submit a Message</h2>
        <form method="POST">
            {% csrf_token %}
            <div class="form-group">
            <textarea
                class="form-control"
                name="content"
                rows="5"
                required
            ></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        </div>
    </body>
    </html>
    ```

### Step 7: Configure .gitignore and push to GitHub

1. Create a .gitignore file in the project root:

    ```.gitignore
    venv/
    __pycache__/
    db.sqlite3
    *.pyc
    *.log
    .DS_Store
    ```

2. Add python libraries to the requirements.txt

    ```bash
    pip freeze > requirements.txt
    ```

3. Initalise git and make the first commit:

    ```bash
    git init 
    git add .
    git commit -m "Initial commit"
    ```

4. Push to GitHub:

    - Create a repo on GitHub
    - Add the GitHub remote, replace your_repo_url with your GitHub repo URL:

    ```bash
    git remote add origin repo_url
    ```

    - Push the code:

    ```bash
    git push -u origin main
    ```

### Step 8: Run and Test the Application

1. Run the Danjgo development server:

    ```bash
    python manage.py runserver
    ```

2. Visit your pages:

    - Go to `http://127.0.0.1:8000/` for home.html
    - Go to `http://127.0.0.1:8000/form` for form.html

### Step 9: Deploy the project on render

1. Create build.sh file

    ```bash
    #!/usr/bin/env bash

    pip install -r requirements.txt
    pip install gunicorn

    # Apply migrations
    python manage.py migrate
    ```

2. Add the domain to the ALLOWED_HOSTS in the setting.py file of the project.
3. In the render build command write the following `./build.sh`.
4. In the start command write the following `gunicorn main.wsgi:application`.
5. Add the enviorment variables and deploy it.
6. For your static files to work in production you might need whitenoise package.
   `pip install whitenoise` and `pip freeze > requirement.txt`. Add the following lines to the middlewares in `settings.py`.
   ```python
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
   ``` 
