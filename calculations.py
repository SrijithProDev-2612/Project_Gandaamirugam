# calculations.py

def calculate_results(student, config):
    total_scored = 0
    total_max = 0

    for exam, subjects in config["exams"].items():
        for subject, max_marks in subjects.items():
            total_scored += student["marks"][exam][subject]
            total_max += max_marks

    percentage = (total_scored / total_max) * 100

    if percentage >= 91:
        grade = "A+"
    elif percentage >= 81:
        grade = "A"
    elif percentage >= 71:
        grade = "B"
    elif percentage >= 61:
        grade = "C"
    elif percentage >= 51:
        grade = "D"
    else:
        grade = "E"

    return total_scored, total_max, round(percentage, 2), grade
