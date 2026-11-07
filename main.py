import csv
import os

SUBJECTS = ["Python", "Database", "Java", "C++", "HTML", "Theory of Computation"]
PASS_MARK = 40
CGPA_SCALE = 10


def get_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
        except ValueError:
            print("Please enter a number.")
            continue

        if 0 <= mark <= 100:
            return mark
        print("Marks must be between 0 and 100.")


def get_grade(mark):
    if mark >= 90:
        return "A+"
    if mark >= 80:
        return "A"
    if mark >= 70:
        return "B"
    if mark >= 60:
        return "C"
    if mark >= 50:
        return "D"
    if mark >= PASS_MARK:
        return "E"
    return "F"


def get_feedback(average):
    if average >= 90:
        return "Outstanding work—keep challenging yourself!"
    if average >= 75:
        return "Great progress. A little extra practice can take you further."
    if average >= 60:
        return "Good effort. Review your weaker subjects to improve."
    if average >= PASS_MARK:
        return "You passed, but a focused study plan will help you improve."
    return "Keep going—review the fundamentals and ask for support where needed."


def main():
    print("=" * 48)
    print("          STUDENT MARKS ANALYZER")
    print("=" * 48)

    while True:
        name = input("Enter student full name: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    marks = {subject: get_mark(subject) for subject in SUBJECTS}
    total = sum(marks.values())
    average = total / len(SUBJECTS)
    cgpa = average / 100 * CGPA_SCALE
    passed = all(mark >= PASS_MARK for mark in marks.values())
    best_subject = max(marks, key=marks.get)
    focus_subject = min(marks, key=marks.get)

    print("\n" + "-" * 48)
    print(f"REPORT CARD: {name}")
    print("-" * 48)
    print(f"{'Subject':<25}{'Marks':>10}{'Grade':>10}")
    print("-" * 48)
    for subject, mark in marks.items():
        print(f"{subject:<25}{mark:>9.2f}{get_grade(mark):>10}")

    print("-" * 48)
    print(f"Total: {total:.2f} / {len(SUBJECTS) * 100}")
    print(f"Average: {average:.2f}%")
    print(f"Estimated CGPA (10-point scale): {cgpa:.2f} / {CGPA_SCALE}")
    print(f"Overall grade: {get_grade(average)}")
    print(f"Result: {'PASS' if passed else 'NEEDS IMPROVEMENT'}")
    print(f"Strongest subject: {best_subject} ({marks[best_subject]:.2f})")
    print(f"Focus subject: {focus_subject} ({marks[focus_subject]:.2f})")
    print(f"Insight: {get_feedback(average)}")
    print("-" * 48)


    filename = "student_Results.csv"
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists or os.path.getsize(filename) == 0:
            writer.writerow(
                ["Name"] + SUBJECTS + [
                    "Total", "Average", "Overall Grade", "Result",
                    "Strongest Subject", "Focus Subject", "Insight",
                ]
            )
        writer.writerow(
            [name]
            + [marks[subject] for subject in SUBJECTS]
            + [
                total,
                average,
                get_grade(average),
                "PASS" if passed else "NEEDS IMPROVEMENT",
                best_subject,
                focus_subject,
                get_feedback(average),
            ]
        )
    print(f"\nData saved to {filename}.")


if __name__ == "__main__":
    main()
