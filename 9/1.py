import re

def validate_passw(passw):
    passw = str(passw)
    if not re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$", passw):
        return "Wrong password"
    else:
        return "Password is valid"

print(validate_passw("rezatnbjhA2"))