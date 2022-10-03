from flask import Flask, render_template, request
from models import Song, Author
import re

app = Flask(__name__)


@app.route('/', methods=['get'])
def index():
    context = {'songs': Song.select()}
    return render_template('index.html', **context)


@app.route('/add_song', methods=['get', 'post'])
def add_song():
    context = {'authors': Author.select()}
    if request.method == 'POST':
        duration = request.form['duration'].strip()
        if not re.match(r'\d{2}:\d{2}', duration):
            context = {'message': "Час вказано невірно(формат XX:CC, наприклад 05:33)"}
            return render_template('message.html', **context)
        if request.form['author'] == 'Автор тексту':
            context = {'message': "Ви не обрали автора"}
            return render_template('message.html', **context)
        Song(
            name=request.form['name'],
            year=request.form['year'],
            author=request.form['author'],
            duration="00:" + request.form['duration'].strip()
        ).save()
        context = {'message': "Пісню додано успішно"}
        return render_template('message.html', **context)
    return render_template('add_song.html', **context)


@app.route('/del_song', methods=['get', 'post'])
def del_song():
    context = {'songs': Song.select()}
    if request.method == 'POST':
        if request.form['song'] == 'Оберіть пісню, яку бажаєте видалити':
            context = {'message': "Такої пісні не існує"}
            return render_template('message.html', **context)
        Song.delete().where(Song.id == request.form['song']).execute()
        context = {'message': "Пісню видалено успішно"}
        return render_template('message.html', **context)
    return render_template('del_song.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
