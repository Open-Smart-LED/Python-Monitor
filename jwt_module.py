import jwt as pyjwt
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException, Header
from database_module import add_esp
def create_jwt(esp_id):
    SECRET = "Your Password" # Check before push

    payload = {
        "id": esp_id,
        "exp": datetime.now(timezone.utc) + timedelta(days=1)
    }

    token = pyjwt.encode(payload, SECRET, algorithm="HS256")
    print("add esp")
    add_esp(esp_id, token)
    return

def verify_token(authorization: str = Header(...)):
    SECRET = "Your Password" # Check before push
    try:
        scheme, token = authorization.split()
        if scheme.lower() != "bearer":
            raise ValueError("Invalid scheme")
        payload = pyjwt.decode(token, SECRET, algorithms=["HS256"])
        return payload
    except Exception as e:
        raise HTTPException(status_code=401, detail="Invalid token")