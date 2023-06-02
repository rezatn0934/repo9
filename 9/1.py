import re

def validate_passw(passw):
    passw = str(passw)
    if not re.search("[a-z]|[A-Z]|[0-9]{8,}", passw):
        raise ValueError("pWrong password")

