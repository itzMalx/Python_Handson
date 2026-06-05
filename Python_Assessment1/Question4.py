import data_validator as dv
import data_processor as dp

print("Enter the number of records to be inserted: ")
n = int(input())


for i in range(n):
    print(f"\nRecord {i+1}:")
    user = input("Enter username: ")
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")

    is_usn = dv.validate_usn(user)
    is_email = dv.email_validator(email)
    is_phone = dv.validate_phone(phone)

    if is_usn:
        print("Valid USN")
    else:
        print("Invalid USN")

    if is_email:
        print("Valid Email")
    else:
        print("Invalid Email")

    if is_phone:
        print("Valid Phone")
    else:
        print("Invalid Phone")

    if is_usn and is_email and is_phone:
        result = dp.data_processor(user, name, email, phone)
    else:
        print("Record is invalid")