# main.py

from config import get_exam_configuration
from input_handler import get_student_data
from pdf_generator import generate_pdf

def main():
    print("📘 SCHOOL MARKSHEET GENERATOR")

    config = get_exam_configuration()

    while True:
        student = get_student_data(config)
        generate_pdf(student, config)
        print("✅ Marksheet generated successfully.")

        cont = input("\nAdd another student? (y/n): ").lower()
        if cont != 'y':
            break

    print("\n🎉 All marksheets generated. Check the 'output' folder.")

if __name__ == "__main__":
    main()
