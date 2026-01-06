school_data = {
    "students": []
}

def add_student(student_record):
    school_data["students"].append(student_record)

def get_all_students():
    return school_data["students"]