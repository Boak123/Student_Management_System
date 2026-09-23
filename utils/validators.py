from config.settings import PASSING_SCORE

def validate_score(score):
    return 0 <= score <= 100

def has_passed(score):
    return score >= PASSING_SCORE

def validate_salary(salary):
    return salary >= 0

def validate_phone(phone):
    return len(phone) > 0 and phone.isdigit()

def validate_name(name):
    return bool(name) and name.replace(" ", "").isalpha()

def validate_student_id(student_id):
    return len(student_id) == 5 and student_id.startswith("ST") and student_id[2:].isdigit()

def validate_email(email):
    return "@" in email and "." in email

def validate_student_data(name, phone, student_id, score):
    return (validate_name(name) and validate_phone(phone) and validate_student_id(student_id) and validate_score(score))




