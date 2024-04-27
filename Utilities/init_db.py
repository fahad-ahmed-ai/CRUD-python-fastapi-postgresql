from database import SessionLocal
from models import User
from .config import user_name,user_password
import bcrypt
from .db_functions import get_user, add_record

def init_db() -> None:
    db = SessionLocal()
    password = user_password.encode("utf-8")

    salt = bcrypt.gensalt()

    hashed_password = bcrypt.hashpw(password, salt)


    db_user =  get_user(user_name)
    if not db_user:
        db_object = User(
        user_name = user_name,
        password = hashed_password.decode("utf-8")
        )
        add_record(db_object)
        print("User Created Successfully")