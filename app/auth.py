from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from dotenv import load_dotenv
import os

load_dotenv()

security = HTTPBasic()

USERNAME = os.getenv("BASIC_AUTH_USERNAME")
PASSWORD = os.getenv("BASIC_AUTH_PASSWORD")

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != USERNAME or credentials.password != PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
