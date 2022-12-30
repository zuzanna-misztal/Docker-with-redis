from flask import Flask, request, render_template
from redis import Redis

app = Flask(__name__, template_folder="templates")

redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/write')
def write_form():
    return render_template('write.html')

@app.route('/write', methods=['POST'])
def write_post():
    first = request.form['first']
    last = request.form['last']
    redis.set(first, last)
    return render_template('writereturn.html', data=(first,last))

@app.route('/get')
def get():
    return render_template('getform.html')

@app.route('/get', methods=['GET', 'POST'])
def get_post():
    first = request.form['first']
    last = redis.get(first)
    if last:
        last = last.decode()
    return render_template('getreturn.html', data=(first,last))


if __name__ == '__main__':
    app.run(host='0.0.0.0')