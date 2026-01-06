# config.py

def get_exam_configuration():
    config = {}

    print("\n--- CLASS CONFIGURATION ---")
    config["school_name"] = input("School name: ").strip()
    config["academic_year"] = input("Academic year (e.g. 2025-26): ").strip()
    config["class_name"] = input("Class (e.g. 10-A): ").strip()

    exams = {}
    num_exams = int(input("Number of exams conducted: "))

    for i in range(num_exams):
        print(f"\nExam {i+1}")
        exam_name = input("Exam name: ").strip()
        subjects = {}

        num_subjects = int(input(f"Number of subjects in {exam_name}: "))
        for j in range(num_subjects):
            subject = input(f"  Subject {j+1} name: ").strip()
            max_marks = int(input(f"  Max marks for {subject}: "))
            subjects[subject] = max_marks

        exams[exam_name] = subjects

    config["exams"] = exams
    return config
