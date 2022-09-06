from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from pbank.auth import login_required
from pbank.db import get_db
from pbank.helpers import deposit

bp = Blueprint('bank', __name__)

@bp.route('/')
def index():
  return render_template('bank/index.html')

@bp.route('/balance', methods=('GET', 'POST'))
@login_required
def balance():
  db = get_db()
  balance = db.execute(
    'SELECT Fifty, Twenty, Ten, Five, Two, One, Fifty_Pence, Twenty_Pence, Ten_Pence, Five_Pence, Two_Pence, One_Pence'
    ' FROM bank WHERE user_id = ?', str(g.user['id'])
  ).fetchone()

  if request.method == "POST":
    balance_input = request.form
    if balance_input['form-button'] == 'deposit':
      deposit(balance_input, str(g.user['id']))
      # db.execute(
      #   'UPDATE bank SET Fifty = Fifty + ?, Twenty = Twenty + ?, Ten = Ten + ?, Five = Five + ?, Two = Two + ?, One = One + ?, Fifty_Pence = Fifty_Pence + ?, Twenty_Pence = Twenty_Pence + ?, Ten_Pence = Ten_Pence + ?, Five_Pence = Five_Pence + ?, Two_Pence = Two_Pence + ?, One_Pence = One_Pence + ? '
      #   'WHERE user_id = ?', (return_val(balance_input['Fifty']), return_val(balance_input['Twenty']), return_val(balance_input['Ten']), return_val(balance_input['Five']),
      #   return_val(balance_input['Two']),return_val(balance_input['One']), return_val(balance_input['Fifty_Pence']), return_val(balance_input['Twenty_Pence']),
      #   return_val(balance_input['Ten_Pence']), return_val(balance_input['Five_Pence']),return_val(balance_input['Two_Pence']), return_val(balance_input['One_Pence']), str(g.user['id']))
      # )
      # db.commit()
    elif balance_input['form-button'] == 'withdraw':
      db.execute(
        'UPDATE bank SET Fifty = Fifty - ?, Twenty = Twenty - ?, Ten = Ten - ?, Five = Five - ?, Two = Two - ?, One = One - ?, Fifty_Pence = Fifty_Pence - ?, Twenty_Pence = Twenty_Pence - ?, Ten_Pence = Ten_Pence - ?, Five_Pence = Five_Pence - ?, Two_Pence = Two_Pence - ?, One_Pence = One_Pence - ? '
        'WHERE user_id = ?', (return_val(balance_input['Fifty']), return_val(balance_input['Twenty']), return_val(balance_input['Ten']), return_val(balance_input['Five']),
        return_val(balance_input['Two']),return_val(balance_input['One']), return_val(balance_input['Fifty_Pence']), return_val(balance_input['Twenty_Pence']),
        return_val(balance_input['Ten_Pence']), return_val(balance_input['Five_Pence']),return_val(balance_input['Two_Pence']), return_val(balance_input['One_Pence']), str(g.user['id']))
      )
      db.commit()
    return redirect('/balance')

  return render_template('bank/balance.html', balance=balance)

