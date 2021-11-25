from passlib.context import CryptContext


# use for hashing the get password within User_table
pwd_context = CryptContext(schemes=["bcrypt"], deprecated= "auto")

def hash(password: str):
    """ Generate Hashed password"""
    return pwd_context.hash(password)

def verifypassword(raw_password, hashed_password):
    """ Generating hashed password from user's raw input """
    return pwd_context.verify(raw_password, hashed_password)