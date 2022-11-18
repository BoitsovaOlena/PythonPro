FROM python:3.8

ENV PYTHONUNBUFFERED=1

# створюємо та відкриваємо директорію для нашого проєкту
RUN mkdir /app
WORKDIR /app

# копіюємо з поточної папки в потону папку контейнера(app)
COPY . .

#інсталюємо пакети
RUN pip install -r requirements.txt
#запускаємо сервер
#CMD python manage.py runserver 0.0.0.0:8000

