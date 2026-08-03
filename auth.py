from fastapi import Request, HTTPException
import jwt
SECRET_KEY="abcdefghijklmnopqrtuvwxyz"
ALGORITHM="HS256"

def authenticated_user(request: Request):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401, detail="Login required")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return payload

def authorize_user(request: Request, required_role: list):
    role_type = authenticated_user(request)

    if role_type.get("role") not in required_role:
        return HTTPException(status_code=403, detail="You do not have permission to access this resource")
    return role_type

