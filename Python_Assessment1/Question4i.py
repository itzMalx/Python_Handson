import re

email_pattern = r'^[A-Za-z0-9.]+@[A-Za-z0-9.]+\.[A-Za-z]{2,5}$'
phone_pattern = r'^[6-9][0-9]{9}$'
user_pattern = r'^25MCA\d{3}$'
def email_validator(email):
    if not email:
        return False
    return bool(re.search(email_pattern, email.strip()))

def validate_phone(phone):
    if not phone:
        return False
    return bool(re.search(phone_pattern, phone.strip()))


def validate_usn(usn):
    if not usn:
        return False
    return bool(re.search(user_pattern, usn.strip()))

def data_processor(user, name, email, phone):
    return {
        "user": user,
        "name": name,
        "email": email,
        "phone": phone,
    }
