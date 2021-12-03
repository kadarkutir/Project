from lib import db

class db_funcs:

    @staticmethod
    def update_plus(amount,user):
        db.execute("UPDATE wallet SET Tokens = Tokens + ? WHERE UserID = ?", amount , user)
        db.commit()

    @staticmethod
    def update_minus(amount,user):
        db.execute("UPDATE wallet SET Tokens = Tokens - ? WHERE UserID = ?", amount , user)
        db.commit()

    @staticmethod
    def select(user):
        token = db.record("SELECT Tokens FROM wallet WHERE UserID = ?",user)
        pure_token = str(token).rstrip(",)").lstrip("(")

        return pure_token

    @staticmethod
    def update_plus_5(amount,user):
        db.execute("UPDATE wallet SET Tokens = Tokens + (?)*5 WHERE UserID = ?", amount , user)
        db.commit()