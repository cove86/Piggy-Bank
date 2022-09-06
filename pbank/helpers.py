import imp
from webbrowser import get
from pbank.db import get_db

def return_val(val):
  return val if val != "" else "0"


def deposit(new_balance, user_id):
  db = get_db()
  db.execute(
      'UPDATE bank SET Fifty = Fifty + ?, Twenty = Twenty + ?, Ten = Ten + ?, Five = Five + ?, Two = Two + ?, One = One + ?, Fifty_Pence = Fifty_Pence + ?, Twenty_Pence = Twenty_Pence + ?, Ten_Pence = Ten_Pence + ?, Five_Pence = Five_Pence + ?, Two_Pence = Two_Pence + ?, One_Pence = One_Pence + ? '
      'WHERE user_id = ?', (new_balance['Fifty'], new_balance['Twenty'], new_balance['Ten'], new_balance['Five'],new_balance['Two'],new_balance['One'], new_balance['Fifty_Pence'], new_balance['Twenty_Pence'],new_balance['Ten_Pence'], new_balance['Five_Pence'],new_balance['Two_Pence'], new_balance['One_Pence'], user_id)
    )
  db.commit()


def withdraw(balance, new_balance, user_id):
  db = get_db()
  db.execute(
    'UPDATE bank SET Fifty = ?, Twenty = ?, Ten = ?, Five = ?, Two = ?, One = ?, '
    'Fifty_Pence = ?, Twenty_Pence = ?, Ten_Pence = ?, Five_Pence = ?, Two_Pence = ?', 
    'One_Pence = ? WHERE user_id = ?', 
  )