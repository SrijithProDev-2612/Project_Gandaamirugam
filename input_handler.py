# input_handler.py

def get_student_data(config):
    student = {}

    print("\n--- STUDENT DETAILS ---")
    student["name"] = input("Student name: ").strip()
    student["roll"] = input("Roll number: ").strip()

    marks = {}

    for exam, subjects in config["exams"].items():
        print(f"\nMarks for {exam}")
        marks[exam] = {}

        for subject, max_marks in subjects.items():
            while True:
                try:
                    score = float(input(f"  {subject} (Max {max_marks}): "))
                    if 0 <= score <= max_marks:
                        marks[exam][subject] = score
                        break
                    else:
                        print("❌ Invalid marks.")
                except ValueError:
                    print("❌ Enter a number.")

    student["marks"] = marks
    return student