from django.contrib import admin
from .models import Profile

# Register your models here.

admin.site.register(Profile)
# Compare this snippet from Elearning/settings.py:
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',

