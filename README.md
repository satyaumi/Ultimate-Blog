# 📝 Ultimate Blogs – Django Blog Application

👨‍💻 Author

Satya Sundar Malik

🔗 **Live Website:**  
https://deveopsatya.pythonanywhere.com/

Ultimate Blogs is a full-featured Django-based blogging platform with authentication, password reset via email, admin management, and production deployment on PythonAnywhere.

---

## 🚀 Features

- User Registration & Login
- Password Reset via Email (Gmail SMTP)
- Secure Custom Logout (POST-based)
- Django Admin Panel
- Blog CRUD Operations
- Categories & Search
- Production Deployment on PythonAnywhere

---

## 🛠️ Tech Stack

- Backend: Django (Python)
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite
- Email Service: Gmail SMTP
- Hosting: PythonAnywhere
- Version Control: Git & GitHub

---

## 📂 Project Creation Flow (From Start to End)

1. Create virtual environment  
2. Install Django  
3. Start Django project  
4. Create apps (`blogs`, `accounts`)  
5. Configure settings  
6. Apply migrations  
7. Create superuser  
8. Build authentication & blog features  
9. Configure email & security  
10. Deploy on PythonAnywhere  

---

## ⚙️ Local Setup Instructions

python -m venv env
env\Scripts\activate        # Windows
source env/bin/activate     # Linux/Mac
pip install django
django-admin startproject blog_main
cd blog_main
python manage.py startapp blogs
python manage.py startapp accounts
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
---
## 🔐 Authentication Configuration

1. Django built-in authentication is enabled using:

2. path("accounts/", include("django.contrib.auth.urls")),


Features provided:

Login

Logout

Password reset

Password reset confirmation
---
🔑 Email Configuration (Secure & Production-Ready)

Email credentials are NOT hardcoded and are loaded using environment variables.

import os

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


Notes:

One sender email can send reset emails to all users

Each user must have a valid email and be active

Password reset works only for users existing in the same database

🚪 Secure Custom Logout Implementation
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from django.shortcuts import redirect

@require_POST
def custom_logout(request):
    logout(request)
    return redirect('home')


Template usage:

<form method="post" action="{% url 'logout' %}">
    {% csrf_token %}
    <button class="btn btn-danger">Logout</button>
</form>

🎨 Static Files Configuration (Admin UI Fix)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

python manage.py collectstatic --noinput

✅ Pre-Deployment Checklist

DEBUG = False

ALLOWED_HOSTS configured

No secrets pushed to GitHub

.env added to .gitignore

STATIC_ROOT configured

Migrations applied

Superuser created

Password reset tested

Static files collected

🌍 PythonAnywhere Deployment (Complete)
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
mkvirtualenv blogenv --python=/usr/bin/python3.11
workon blogenv
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput


PythonAnywhere Web Tab Configuration:

Source code: /home/username/yourrepo

Virtualenv: /home/username/.virtualenvs/blogenv

Static files mapping:

URL	Directory
/static/	/home/username/yourrepo/staticfiles

Environment Variables (Web Tab):

EMAIL_HOST_USER = yourgmail@gmail.com

EMAIL_HOST_PASSWORD = gmail_app_password

Reload the web app after configuration.

🧪 Post-Deployment Testing

Admin panel UI loads correctly

Login & Logout works

Password reset email is delivered

Blog creation & listing works

Static files load correctly

🔐 Security Notes

Never commit credentials to GitHub

Rotate Gmail App Password if exposed

Logout must always be POST-based

Local and production databases are separate

