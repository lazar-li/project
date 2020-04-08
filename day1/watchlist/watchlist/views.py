from watchlist import app,db
from flask import Flask,url_for,render_template,request,flash,redirect
from flask_login import login_user,logout_user,login_required,current_user
from watchlist.models import User,Movie


#views  视图函数
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


