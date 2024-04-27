from fastapi import Request, Depends
from .schemas import UserCreate, Userlogin, Transaction_Schema
from models import User, Transaction
from Utilities.db_functions import get_user
from database import SessionLocal
import bcrypt
from auth.auth_handler import access_token
from auth.auth_handler import get_current_user
from Utilities.errors import success_response, not_found_response,\
                             unauthorized_response, error_response
from uuid import UUID


async def create_user(Create_Model:UserCreate):
    db = SessionLocal()
    try :
        username = Create_Model.user_name
        db_user = get_user(username)

        print(Create_Model.password)
        password = Create_Model.password.encode("utf-8")

        salt = bcrypt.gensalt()

        hashed_password = bcrypt.hashpw(password, salt)

        if db_user:
            perm_err = unauthorized_response(msg="User Already Exists")
            return perm_err
        else:

            db_object = User(
            user_name = Create_Model.user_name,
            password = hashed_password.decode("utf-8")
            )
            db.add(db_object)
            db.commit()
            db_object_id = db_object.id
            return {
                    "error": "",
                    "msg": "User Created Successfully",
                    "data": {
                            "id": db_object_id,
                            },
                    "status_code": 200
                    }
    except Exception as e:
       response = error_response(msg="Failed", exception=e)
       return  response
    


async def login(request: Request,login_model:Userlogin):
    db = SessionLocal()
    try:
        username = login_model.user_name
        db_user = get_user(username)
        if db_user:

            stored_hashed_password = db_user.password.encode()
            if bcrypt.checkpw(login_model.password.encode("utf-8"),\
                            stored_hashed_password):

                token = access_token(str(db_user.id))
                return {
                        "error": "",
                        "msg": "Login Successfully",
                        "data": {
                                "id": db_user.id,
                                "Token": token
                                },
                        "status_code": 200
                    }


            else:
                perm_err = unauthorized_response(msg="Enter Valid Name & Password")
                return perm_err
        else:
            perm_err = unauthorized_response(msg="Enter Valid Name & Password")
            return perm_err
    except Exception as e:
       response = error_response(msg="Failed", exception=e)
       return  response   



async def create_transaction(Create_Trans:Transaction_Schema,\
                            user_id: int = Depends(get_current_user)):
    db = SessionLocal()
    try:
        db_object = Transaction(
                                amount = Create_Trans.amount,
                                description = Create_Trans.description,
                                user_id = user_id

                                )
        db.add(db_object)
        db.commit()
        db_object_id = db_object.id
        return {
                        "error": "",
                        "msg": "Transaction Successful",
                        "data": {
                                "id": db_object_id,
                                },
                        "status_code": 200
                        }
    except Exception as e:
       response = error_response(msg="Failed", exception=e)
       return  response
    


async def get_transactions(user_id: int = Depends(get_current_user)):
    db = SessionLocal()
    print(user_id)
    try:
        transactions_deatils = db.query(Transaction).filter(Transaction.user_id == user_id).all()
        if transactions_deatils:
            return transactions_deatils
        else:
            perm_err = not_found_response(msg="You Have no Transactions")
            return perm_err
    except Exception as e:
       response = error_response(msg="Failed", exception=e)
       return  response
    
    
async def update_transaction(transaction_id: UUID,
                            Update:Transaction_Schema,\
                               user_id: int = Depends(get_current_user)):
    db = SessionLocal()
    try:

            get_data = db.query(Transaction).filter(Transaction.id == transaction_id).first()
            if get_data:
                if get_data.user_id == user_id:
                    db.query(Transaction).filter_by(id=get_data.id).update(
                        {
                            "amount" : Update.amount,
                            "description" : Update.description,

                        }
                    )

                    db.commit()
                    db.refresh(get_data)
                    succes = success_response(msg="Transaction Updated Successfully")
                    return succes
            
                else:
                    err = not_found_response(msg="Transaction Not Found")
                    return err
            else:
                    err = not_found_response(msg="Transaction Not Found")
                    return err
    except Exception as e:
       response = error_response(msg="Failed", exception=e)
       return  response
    


async def delete_transaction(transaction_id: UUID,
                             user_id: int = Depends(get_current_user)):
    db = SessionLocal()
    try:

        get_data = db.query(Transaction).filter(Transaction.id == transaction_id).first()
        if get_data:
            if get_data.user_id == user_id:
                db.delete(get_data)
                db.commit()
                succes = success_response(msg="Transaction Deleted Successfully")
                return succes
            else:
                succes = not_found_response(msg="Transaction Not Found")
                return succes
        else:
            err = not_found_response(msg="Transaction Not Found")
            return err
    except Exception as e:
       response = error_response(msg="Failed", exception=e)
       return  response
