DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS bank;
DROP TRIGGER IF EXISTS trg_bank;

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

CREATE TRIGGER trg_bank
AFTER INSERT ON user
BEGIN
  INSERT INTO bank(
    user_id,
    Fifty,
    Twenty,
    Ten,
    Five,
    Two,
    One,
    Fifty_Pence,
    Twenty_Pence,
    Ten_Pence,
    Five_Pence,
    Two_Pence,
    One_Pence
  )
  VALUES
  (
    NEW.id,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
  );
  END;