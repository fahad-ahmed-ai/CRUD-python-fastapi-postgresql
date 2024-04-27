from database import SessionLocal
from models import User


def get_user(username):
    db = SessionLocal()
    user = db.query(User).filter(User.user_name == username).first()
    return user

def add_record(db_object):
    db = SessionLocal()
    db.add(db_object)
    db.commit()