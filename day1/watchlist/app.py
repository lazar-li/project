#系统库
import os,sys
import click
from flask import Flask,url_for,render_template
from flask_sqlalchemy import SQLAlchemy
#用来测试  是不是win的系统
WIN = sys.platform.startswith('win')
if WIN:
    prefix = "sqlite:///"#swindows  平台
else:
    perfix = "sqlite:////"#Max   Linun 平台


app = Flask(__name__)

#用来配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = prefix+os.path.join(app.root_path,'date.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app)


#-----------------------------models-------------------------------------------------------

class User(db.Model):
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(20))


class Movie(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))
#------------------------------------------------------------------------------------------clear
@app.route('/')

def index1():

    user = User.query.first()
    movies = Movie.query.all()

    return render_template('index.html',name=user,movies=movies)


#自定义命令

@app.cli.command()#注册为命令
@click.option('--drop',is_flag=True,help="先删除在创建")
def initdb(drop):
    if drop:
        db.drop_all()
    db.create_all()
    #输出一句话的话是  
    click.echo("初始化数据库完成")




#向空数据种插入数据


@app.cli.command()
def forge():
    name = "lazar"
    movies = [
        {"title":"大赢家","year":"2020.12.29"},
        {"title":"复仇者联盟","year":"2020.12.29"},
        {"title":"疯狂外星人","year":"2019"},
        {"title":"叶问","year":"2017"},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movies = Movie(title=m['title'],year=m['year'])
        db.session.add(movies)
    db.session.commit()
    click.echo("导入数据完成")

#404 报错信息
@app.errorhandler(404)
def page_not_found(e):
    user = User.query.first()
    return render_template('404.html',user=user)
if __name__ == '__main__':
    app.run(debug=True)