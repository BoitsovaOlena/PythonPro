from django.conf import settings
from online_school.celery import app
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

@app.task
def add_token():
    for user in get_user_model().objects.all():
        tokens = Token.objects.filter(user=user)
        if len(tokens) > 0:
            tokens[0].delete()
        Token.objects.create(user=user)

