from flask import Flask, render_template, request
from utils import get_equal_sentence
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        input_sentence = request.form['input-sentence']
        res = get_equal_sentence(input_sentence)
        return render_template('index.html', res=res, inp=input_sentence)
    return render_template('index.html', res='', inp='')


if __name__ == '__main__':
    app.run()
