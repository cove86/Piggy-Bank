DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS bank;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE bank (
  user_id INTEGER NOT NULL,
  Fifty INTEGER,
  Twenty INTEGER,
  Ten INTEGER,
  Five INTEGER,
  Two INTEGER,
  One INTEGER,
  Fifty_Pence INTEGER,
  Twenty_Pence INTEGER,
  Ten_Pence INTEGER,
  Five_Pence INTEGER,
  Two_Pence INTEGER,
  One_Pence INTEGER,
  FOREIGN KEY (user_id) REFERENCES user (id)
);