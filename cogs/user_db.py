# Commands to read data from user_db.json

import json

with open("./user_db.json") as f:
    db = json.load(f)

def is_user(user):
    try:
        db["users"][user]
        return True
    except:
        return False

def get_user(user):
    if not is_user(user): return False

    return db["users"][user]

def get_xp(user):
    if not is_user(user): return False

    return db["users"][user]["xp"]

def get_tournaments(user):
    if not is_user(user): return False

    return db["users"][user]["tournaments"]

def get_lichess_acc(user):
    if not is_user(user): return False

    return db["users"][user]["lichess_acc"]