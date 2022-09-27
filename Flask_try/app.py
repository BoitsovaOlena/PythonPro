from flask import Flask, render_template, request
from faker import Faker
from library import check_request
fake = Faker()
app = Flask(__name__)


@app.route('/', methods=['get'])
def index():
    return render_template('index.html')


@app.route('/requirements', methods=['get'])
def requirements():
    context = {}
    with open('../requirements.txt', 'rt') as file:
        context['requirements'] = file.read().split('\n')
    return render_template('requirements.html', **context)


@app.route('/generate-users', methods=['get', 'post'])
def generate_users():
    context = {}
    users_amount = 100
    if request.method == 'POST':
        users_amount = int(request.form['users_amount']) if len(request.form['users_amount']) > 0 else users_amount
    users = []
    for i in range(users_amount):
        users.append(f'{Faker(["uk_UA"]).unique.first_name()} {Faker(["en_US"]).lexify(text="??????????@mail.com")}')
        context['users'] = users
    return render_template('users.html', **context)


@app.route('/space', methods=['get'])
def space():
    context = {}
    resp = check_request('http://api.open-notify.org/astros.json', 'application/json').json()
    context["number"] = resp["number"]
    return render_template('space.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
