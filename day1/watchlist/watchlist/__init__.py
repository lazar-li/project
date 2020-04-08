from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os,sys
from flask import Flask
#导入 watchlist  需要用得应用

#--------------------以上模块区----------------------------


app = Flask(__name__)
#---------------------用来测试  是不是win的系统---------------------------------
WIN = sys.platform.startswith('win')
if WIN:
    prefix = "sqlite:///"#swindows  平台
else:
    perfix = "sqlite:////"#Max   Linun 平台
#-----------------------------------------------------------------------------

#用来配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = prefix+os.path.join(os.path.dirname(app.root_path),'date.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '1903_dev'

db = SQLAlchemy(app=app)

login_manager = LoginManager(app)  #实例化扩展类


#装饰器
@login_manager.user_loader
def load_user(user_id):    #这个是在创建用户的加载  回调函数接受用户ID作为阐述
    from watchlist.models import User
    user = User.query.get(user_id)
    return user

#如果操作了需要登录才有的操作
login_manager.login_view = 'login'


#模板上下文处理的函数
@app.context_processor
def common_user():
    from watchlist.models import User
    user = User.query.first()
    return dict(name=user)

from watchlist import views,errors,commands

