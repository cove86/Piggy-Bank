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
    db.execute(
      'UPDATE bank SET Fifty = ?, Twenty = ?, Ten = ?, Five = ?, Two = ?, One = ?, Fifty_Pence = ?, Twenty_Pence = ?, Ten_Pence = ?, Five_Pence = ?, Two_Pence = ?, One_Pence = ? '
      'WHERE user_id = ?', (return_val(request.form['Fifty']), return_val(request.form['Twenty']), return_val(request.form['Ten']), return_val(request.form['Five']),
      return_val(request.form['Two']),return_val(request.form['One']), return_val(request.form['Fifty_Pence']), return_val(request.form['Twenty_Pence']),
      return_val(request.form['Ten_Pence']), return_val(request.form['Five_Pence']),return_val(request.form['Two_Pence']), return_val(request.form['One_Pence']), str(g.user['id']))
    )
    db.commit()

  return render_template('bank/balance.html', data=data)

