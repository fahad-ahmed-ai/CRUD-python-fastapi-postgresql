from datetime import datetime, timedelta
import jwt
from fastapi import HTTPException
from fastapi import Depends, HTTPException, status
from Utilities.config import algorithm, secret
from fastapi.security import HTTPBearer
JWT_SECRET = secret
JWT_ALGORITHM = algorithm
from jose import jwt, ExpiredSignatureError

# payload refers to the data or information that is sent by the client in a request
def token_response(token: str):
    return token


def access_token(db_user: str):
    payload = {
        "exp": datetime.utcnow() + timedelta(hours=1),
        "iat": datetime.utcnow(),
        "scope": "access_token",
        "user_id": db_user,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


bearer_scheme = HTTPBearer(scheme_name="Token")



def get_current_user(token: str = Depends(bearer_scheme)):
    try:
        token_bytes = token.credentials.encode('utf-8')
        payload = jwt.decode(token_bytes, JWT_SECRET, algorithms=JWT_ALGORITHM)
        user_id = payload.get("user_id")
        return user_id
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Token has expired"
        )
    except jwt.JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )