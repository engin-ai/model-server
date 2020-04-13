from flask import Flask, render_template, request

app = Flask(__name__)

ENV = 'dev'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        return render_template('index.html', message='You have already submitted feedback')

if __name__ == '__main__':
    app.run()
