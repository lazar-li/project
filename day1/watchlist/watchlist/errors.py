from watchlist import app

from flask import render_template

#404 报错信息
@app.errorhandler(404)
def page_not_found(e):
    # user = User.query.first()
    return render_template('404.html')
