# Student Marks Analyzer

A simple Python command-line program that collects a student's marks and prints a report card with grades and performance feedback.

## Features

- Collects marks for Python, Database, Java, C++, HTML, and Theory of Computation.
- Checks that each mark is a number between 0 and 100.
- Calculates the total and average.
- Estimates CGPA on a 10-point scale from the average percentage.
- Displays a grade for each subject and an overall grade.
- Reports whether the student passed every subject.
- Highlights the strongest subject and the subject to focus on.
- Provides feedback based on the average.

## Subjects

The analyzer currently collects marks for:

1. Python
2. Database
3. Java
4. C++
5. HTML
6. Theory of Computation

## Technologies used

- **Python 3** — application language
- **Python standard library** — used for program logic and input/output; no third-party packages are required
- **CSV
- **Git
- **GitHub

## Requirements

- Python 3

No third-party packages are required.

## HOW to Run

Open a terminal in the project folder and run:

```bash
python main.py
```

On some Windows installations, use:

```powershell
py main.py
```

Enter the student's name, then enter a mark from 0 to 100 when prompted for each subject. If an entry is not a number or is outside that range, the program asks for it again.

## Grade scale

| Mark | Grade |
|---:|:---|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| 40–49.99 | E |
| Below 40 | F |

The student passes only if their mark is at least 40 in every subject.

## CGPA calculation

The program estimates CGPA using the average percentage:

-text
CGPA = (average percentage / 100) * 10

For example, an average of 80% gives an estimated CGPA of 8.00/10. This is a simple estimate; official CGPA calculations can differ between institutions and may use course credits or a different conversion scale.