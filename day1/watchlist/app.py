#系统库
import os,sys
from flask import Flask,url_for,render_template,request,flash,redirect
from werkzeug.security import generate_password_hash,check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin,login_user,logout_user,login_required,current_user
import click

#---------------------用来测试  是不是win的系统---------------------------------
WIN = sys.platform.startswith('win')
if WIN:
    prefix = "sqlite:///"#swindows  平台
else:
    perfix = "sqlite:////"#Max   Linun 平台
#-----------------------------------------------------------------------------

app = Flask(__name__)

#用来配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = prefix+os.path.join(app.root_path,'date.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1903_dev'

db = SQLAlchemy(app=app)
login_manager = LoginManager(app)  #实例化扩展类


#装饰器
@login_manager.user_loader
def load_user(user_id):    #这个是在创建用户的加载  回调函数接受用户ID作为阐述
    user = User.query.get(user_id)
    return user

#如果操作了需要登录才有的操作
login_manager.login_view = 'login'

#-----------------------------models-------------------------------------------------------

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    def validate_password(self,password):
        return check_password_hash(self.password_hash,password)

class Movie(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))
#------------------------------------------------------------------------------------------clear
@app.route('/',methods=['GET','POST'])

def index1():
    if request.method.lower() == "post":
        if not current_user.is_authenticated:
            return redirect(url_for("index1"))
        title = request.form.get('title')
        year = request.form.get("year")

        #验证数据
        if not title or not year or len(year)>4 or len(title)>60:
            flash('输入错误')
            #重定向
            return redirect(url_for('index1'))
            #将数据保存到数据库
        movie = Movie(title=title,year=year)
        db.session.add(movie)
        db.session.commit()
        flash("创建成功")
        return redirect(url_for('index1'))
    movies = Movie.query.all()
    return render_template('index.html',movies=movies)


#更新数据
@app.route('/movie/edit/<int:movie_id>',methods=["GET","POST"])
@login_required
def edit(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    if request.method == 'POST':
        title = request.form['title']
        year = request.form['year']
        if not title or not year or len(year)>4 or len(title)>60:
            flash('输入有误')
            return redirect(url_for('edit'),movie_id = movie_id)
        movie.title = title
        movie.year = year
        db.session.commit()
        flash('电影更新完成')
        return redirect(url_for('index1'))
    return render_template('edit.html',movie=movie)



#删除数据函数

@app.route('/movie/delete/<int:movie_id>',methods=["GET","POST"])
@login_required
def delete(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('删除完成')
    return redirect(url_for('index1'))






#登录
@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if not username or not password:
            flash("输入有误")
            return redirect(url_for('login'))
        user = User.query.first()
        if username == user.username and user.validate_password(password):
            login_user(user)
            flash("登录成功")
            return redirect(url_for('index1'))
        flash("验证失败")
        return redirect(url_for('login'))
    else:
        return render_template('login.html')

#登录 推出  注销  logout
@app.route('/logout',methods=["POST","GET"])
@login_required
def logout():
    logout_user()
    flash("退出成功")
    return redirect(url_for('index1'))


#设置
@app.route('/settings',methods=["POST","GET"])
@login_required
def settings():
    if request.method == "POST":
        name = request.form['name']
        if not name or len(name)>20:
            flash('输入错误')
            return redirect(url_for("settings"))
        current_user.name = name
        db.session.commit()
        flash("名字已经更新")
        return redirect(url_for('index1')) 
    return render_template("setting.html")




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



#  自定义指令，  生成管理员帐号  flask lazar
#  输入用户名  lazar  密码  确认密码
@app.cli.command()
@click.option('--username',prompt=True,help="管理员的用户名")
#  confirmation_prompt  用来  二次输入密码    hide_input 用来不是铭文   prompt需要输出马
@click.option('--password',prompt=True,help="管理员的密码",confirmation_prompt=True,hide_input=True)
def admin(username,password):
    user = User.query.first()
    if user is not None:
        click.echo('更新管理员用户')
        user.username = username
        user.set_password(password)
    else:
        click.echo("创建管理员帐号")
        user = User(username=username,name="lazar")
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo("管理员帐号更新或者创建完成呢个")




#404 报错信息
@app.errorhandler(404)
def page_not_found(e):
    # user = User.query.first()
    return render_template('404.html')





#模板上下文处理的函数
@app.context_processor
def common_user():
    user = User.query.first()
    return dict(name=user)




if __name__ == '__main__':
    app.run(debug=True)