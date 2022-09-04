from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
from flaskr.helpers import return_val

bp = Blueprint('bank', __name__)

@bp.route('/')
def index():
  return render_template('bank/index.html')

@bp.route('/balance', methods=('GET', 'POST'))
@login_required
def balance():
  db = get_db()
  data = db.execute(
    'SELECT Fifty, Twenty, Ten, Five, Two, One, Fifty_Pence, Twenty_Pence, Ten_Pence, Five_Pence, Two_Pence, One_Pence'
    ' FROM bank WHERE user_id = ?', str(g.user['id'])
  ).fetchone()

  if request.method == "POST":
    print(request.form)
    fifty = return_val(request.form.get('50'))
    print(fifty)

  return render_template('bank/balance.html', data=data)

