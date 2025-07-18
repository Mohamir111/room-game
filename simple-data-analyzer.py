# --- Data Setup ---
student_grades = [
    {"name": "Alice", "subject": "Math", "grade": 85},
    {"name": "Bob", "subject": "Math", "grade": 72},
    {"name": "Alice", "subject": "Science", "grade": 92},
    {"name": "Charlie", "subject": "Math", "grade": 60},
    {"name": "Bob", "subject": "Science", "grade": 78},
    {"name": "Alice", "subject": "History", "grade": 70},
    {"name": "Charlie", "subject": "Science", "grade": 88},
    {"name": "David", "subject": "Math", "grade": 95},
    {"name": "David", "subject": "History", "grade": 81},
    {"name": "Eve", "subject": "Science", "grade": 65}
]

# --- Functions ---
def get_all_grades(data):
    """Extracts all numerical grades from the dataset."""
    grades = []
    for record in data:
        grades.append(record["grade"])
    return grades

def calculate_average_grade(grades_list):
    """Calculates the average of a list of grades. Handles empty list."""
    if not grades_list:
        return 0.0
    return sum(grades_list) / len(grades_list)

def find_highest_grade(grades_list):
    """Finds the highest grade in a list. Handles empty list."""
    if not grades_list:
        return None
    highest = grades_list[0]
    for grade in grades_list:
        if grade > highest:
            highest = grade
    return highest

def find_lowest_grade(grades_list):
    """Finds the lowest grade in a list. Handles empty list."""
    if not grades_list:
        return None
    lowest = grades_list[0]
    for grade in grades_list:
        if grade < lowest:
            lowest = grade
    return lowest

def get_grades_by_subject(data, subject_name):
    """Extracts all grades for a specific subject."""
    grades = []
    for record in data:
        if record["subject"].lower() == subject_name.lower():
            grades.append(record["grade"])
    return grades

def get_students_with_passing_grade(data, passing_threshold=70):
    """Returns a list of unique names of students who have at least one passing grade."""
    passing_students = set()
    for record in data:
        if record["grade"] >= passing_threshold:
            passing_students.add(record["name"])
    return sorted(list(passing_students))

def get_student_average_grade(data, student_name):
    """Calculates the average grade for a specific student across all their subjects."""
    student_grades_list = []
    for record in data:
        if record["name"].lower() == student_name.lower():
            student_grades_list.append(record["grade"])
    if not student_grades_list:
        return 0.0
    return sum(student_grades_list) / len(student_grades_list)

def main_analysis_report(data):
    """Orchestrates the calls to the above functions and prints a formatted report."""
    print("\n--- Student Grade Analysis Report ---")

    # Overall Grades
    all_grades = get_all_grades(data)
    unique_students = set(record["name"] for record in data)

    print("\nOverall Grades:")
    print(f" Total Students: {len(unique_students)}")
    print(f" Total Grades: {len(all_grades)}")
    print(f" Average Grade: {calculate_average_grade(all_grades):.2f}")
    print(f" Highest Grade: {find_highest_grade(all_grades)}")
    print(f" Lowest Grade: {find_lowest_grade(all_grades)}")

    # Grades by Subject
    print("\nGrades by Subject:")
    subjects = sorted(list(set(record["subject"] for record in data)))
    for subject in subjects:
        subject_grades = get_grades_by_subject(data, subject)
        if subject_grades:
            print(f" {subject}:")
            print(f"  Average: {calculate_average_grade(subject_grades):.2f}")
            print(f"  Highest: {find_highest_grade(subject_grades)}")
            print(f"  Lowest: {find_lowest_grade(subject_grades)}")

    # Students with Passing Grades
    passing_students_list = get_students_with_passing_grade(data)
    print("\nStudents with Passing Grades (>=70):")
    print(f" {', '.join(passing_students_list)}")

    # Individual Student Averages
    print("\nIndividual Student Averages:")
    for student_name in sorted(list(unique_students)):
        avg_grade = get_student_average_grade(data, student_name)
        print(f" {student_name}: {avg_grade:.2f}")

    print("\n--- End of Report ---")

# --- Run the Report ---
main_analysis_report(student_grades)
