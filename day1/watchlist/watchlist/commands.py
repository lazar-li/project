from watchlist import db,app

from watchlist.models import User,Movie

import click




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

