from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
import os


def generate_pdf(student, config):
    # ---------------- SAFETY ----------------
    os.makedirs("output", exist_ok=True)

    name = student.get("name", "Unknown")
    roll = student.get("roll", "NA")
    marks = student.get("marks", {})

    school_name = config.get("school_name", "School Name")
    academic_year = config.get("academic_year", "Academic Year")
    class_name = config.get("class", "NA")

    exams = list(marks.keys())

    # Collect all subjects
    subjects = set()
    for exam in marks.values():
        subjects.update(exam.keys())
    subjects = sorted(subjects)

    # ---------------- PDF SETUP ----------------
    filename = f"output/{roll}_{name.replace(' ', '_')}.pdf"
    c = canvas.Canvas(filename, pagesize=landscape(A4))
    width, height = landscape(A4)

    # ---------------- LOGO ----------------
    logo_path = "logo.png"
    if os.path.exists(logo_path):
        c.drawImage(
            ImageReader(logo_path),
            width / 2 - 80,
            height - 140,
            width=160,
            height=70,
            mask="auto"
        )

    # ---------------- HEADER ----------------
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width / 2, height - 160, school_name)

    c.setFont("Helvetica", 11)
    c.drawCentredString(width / 2, height - 185, academic_year)

    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, height - 205, exam_title)

    # ---------------- STUDENT INFO ----------------
    c.setFont("Helvetica", 11)
    c.drawString(60, height - 210, f"Student Name : {name}")
    c.drawString(width / 2 - 40, height - 210, f"Roll No : {roll}")
    c.drawString(width - 260, height - 210, f"Class & Section : {class_name}")

    # ---------------- TABLE ----------------
    table_top = height - 245
    row_height = 30
    left_margin = 60
    right_margin = width - 60

    subject_col_width = 220
    exam_col_width = (right_margin - left_margin - subject_col_width) / len(exams)

    # Top border
    c.line(left_margin, table_top, right_margin, table_top)

    # Header row
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left_margin + 25, table_top - 22, "Subject")

    for i, exam in enumerate(exams):
        x = left_margin + subject_col_width + i * exam_col_width + 10
        c.drawString(x, table_top - 22, exam)

    c.line(left_margin, table_top - 40, right_margin, table_top - 40)

    # Data rows
    c.setFont("Helvetica", 11)
    y = table_top - 70
    exam_totals = {exam: 0 for exam in exams}

    for subject in subjects:
        c.drawString(left_margin + 10, y, subject)

        for i, exam in enumerate(exams):
            score = marks.get(exam, {}).get(subject, 0)
            exam_totals[exam] += score
            x = left_margin + subject_col_width + i * exam_col_width + 10
            c.drawString(x, y, str(score))

        y -= row_height

    x_positions = [left_margin, left_margin + subject_col_width]
    for i in range(len(exams)):
        x_positions.append(left_margin + subject_col_width + (i + 1) * exam_col_width)

    for x in x_positions:
        c.line(x, table_top, x, y - 20)

    # Total row
    c.line(left_margin, y + 10, right_margin, y + 10)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(left_margin + 10, y - 5, "Total")

    for i, exam in enumerate(exams):
        x = left_margin + subject_col_width + i * exam_col_width + 10
        c.drawString(x, y - 5, str(exam_totals[exam]))

    c.line(left_margin, y - 20, right_margin, y - 20)

    # ---------------- SIGNATURES ----------------
    c.setFont("Helvetica", 11)
    c.drawString(left_margin, 55, "Class Teacher")
    c.drawRightString(right_margin, 55, "Principal")

    c.save()