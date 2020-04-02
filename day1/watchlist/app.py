from flask import Flask,url_for,render_template


app = Flask(__name__)


# @app.route('/')

# def index():
#     return "good 我爱我老婆江绵"

@app.route('/')

def index1():
    name = "lazar"
    movies = [
        {"title":"大赢家","year":"2020.12.29"},
        {"title":"复仇者联盟","year":"2020.12.29"},
        {"title":"疯狂外星人","year":"2019"},
        {"title":"叶问","year":"2017"},
    ]

    return render_template('index.html',name=name,movies=movies)

if __name__ == '__main__':
    app.run(debug=True)