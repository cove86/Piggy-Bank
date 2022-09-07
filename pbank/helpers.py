import imp
from webbrowser import get
from pbank.db import get_db
from datetime import datetime

def return_val(val):
  return val if val != "" else "0"


def deposit(new_balance, user_id):
  db = get_db()
  db.execute(
      'UPDATE bank SET Fifty = Fifty + ?, Twenty = Twenty + ?, Ten = Ten + ?, Five = Five + ?, Two = Two + ?, One = One + ?, Fifty_Pence = Fifty_Pence + ?, Twenty_Pence = Twenty_Pence + ?, Ten_Pence = Ten_Pence + ?, Five_Pence = Five_Pence + ?, Two_Pence = Two_Pence + ?, One_Pence = One_Pence + ? '
      'WHERE user_id = ?', (new_balance['Fifty'], new_balance['Twenty'], new_balance['Ten'], new_balance['Five'],new_balance['Two'],new_balance['One'], new_balance['Fifty_Pence'], new_balance['Twenty_Pence'],new_balance['Ten_Pence'], new_balance['Five_Pence'],new_balance['Two_Pence'], new_balance['One_Pence'], user_id)
    )
  db.commit()


def withdraw(new_balance, user_id):
  db = get_db()
  
  db.execute(
    'UPDATE bank SET Fifty = ?, Twenty = ?, Ten = ?, Five = ?, Two = ?, One = ?, '
    'Fifty_Pence = ?, Twenty_Pence = ?, Ten_Pence = ?, Five_Pence = ?, Two_Pence = ?,' 
    ' One_Pence = ? WHERE user_id = ?', (new_balance['Fifty'], new_balance['Twenty'], new_balance['Ten'], new_balance['Five'],new_balance['Two'],new_balance['One'], new_balance['Fifty_Pence'], new_balance['Twenty_Pence'],new_balance['Ten_Pence'], new_balance['Five_Pence'],new_balance['Two_Pence'], new_balance['One_Pence'], user_id)
  )
  db.commit()


def enough_to_withdraw(balance, new_balance):
    updated = {}

    for key in new_balance:
      if key != 'form-button':
        updated[key] = balance[key] - int(new_balance[key])
        if updated[key] < 0:
          return -1
    return updated


def tran_history(new_balance, type, user):
  db = get_db()
  history = ''
  date = datetime.now()

  for key in new_balance:
    if key != 'form-button' and int(new_balance[key]) > 0:
      history += key + ' : ' + new_balance[key] + ' '
  
  db.execute(
    'INSERT INTO transaction_history VALUES (?, ?, ?, ?)', (type, history, date, user)
  )
  db.commit()
