# Django Chat App

A simple real-time chat application for Django using AJAX.

## Installation

1. Install the package using pip:
   ```bash
   pip install django-chat-app


2. Add chat to your INSTALLED_APPS in settings.py:

INSTALLED_APPS = [
    ...
    'chat',
]

3. Include the chat URLs in your project's urls.py:

from django.urls import path, include

urlpatterns = [
    ...
    path('chat/', include('chat.urls')),
]

4. Run migrations:

python manage.py migrate