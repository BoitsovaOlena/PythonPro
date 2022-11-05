from django.conf import settings
from django.contrib.auth import get_user_model
from online_school.celery import app
from django.core.mail import send_mail
import datetime
from main.models import Course


@app.task
def send_email_to_admins(data):
    message = f"""
    {data['name']} надіслав вам це повідомлення.\n
    Email: {data['email']}\n
    Телефон: {data.get('phone')}\n
    Текст повідомлення: {data['message']}\n

    """
    send_mail(
        subject="New contact form.",
        from_email="form_mail@online_school.com",
        message=message,
        recipient_list=settings.ADMIN_EMAILS
    )

@app.task
def new_course_email(data):
    emails = get_user_model().objects.all().values_list('email', flat=True)
    message = f"""
        Добрий день. У нашій школі зявився новий курс {data}.
        Детали можна переглянути на нашому сайті http://127.0.0.1:8000/
    """
    for email in emails:
        send_mail(
            subject="New course available.",
            from_email="admin@online_school.com",
            message=message,
            recipient_list=[email]
        )


@app.task
def new_courses_email():
    today = datetime.datetime.now().date()
    courses = Course.objects.filter(created_at__contains=today).values_list('name', flat=True)
    emails = get_user_model().objects.all().values_list('email', flat=True)
    message = f"""
        Перелык нових курсів: {', '.join(courses)}
    """
    for email in emails:
        send_mail(
            subject="New course available.",
            from_email="admin@online_school.com",
            message=message,
            recipient_list=[email]
        )