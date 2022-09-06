from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from pbank.auth import login_required
from pbank.db import get_db
from pbank.helpers import deposit, withdraw, enough_to_withdraw

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
      flash('Deposit Successful')      

    elif balance_input['form-button'] == 'withdraw':
      withdrawn = enough_to_withdraw(balance, balance_input)
      if withdrawn == -1:
        flash('Not Enough Cash')
      else:
        withdraw(withdrawn, str(g.user['id']))
        flash('Withdrawal Successful')
    return redirect('/balance')

  return render_template('bank/balance.html', balance=balance)


@bp.route('/transactions')
@login_required
def transactions():
  return render_template('bank/transactions.html')


@bp.route('/myaccount')
@login_required
def myaccount():
  return render_template('bank/myaccount.html')

