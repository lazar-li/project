from flask import Flask,url_for


app = Flask(__name__)


@app.route('/')

def index():
    return "good 我爱我老婆江绵"

@app.route('/index/<name>')

def index1(name):
    print(url_for('index',name="haha"))
    return "i love {}".format(name)

if __name__ == '__main__':
    app.run(debug=True)