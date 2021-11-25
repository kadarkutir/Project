from lib import db

def update_plus(amount,user):
    db.execute("UPDATE wallet SET Tokens = Tokens + ? WHERE UserID = ?", amount , user)
    db.commit()

def update_minus(amount,user):
    db.execute("UPDATE wallet SET Tokens = Tokens - ? WHERE UserID = ?", amount , user)
    db.commit()


def select(user):
    token = db.record("SELECT Tokens FROM wallet WHERE UserID = ?",user)
    pure_token = str(token).rstrip(",)").lstrip("(")

    return pure_token

