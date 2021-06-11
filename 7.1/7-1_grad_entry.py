"""
    Ask the user how many students are in their class. Get the student's name and final grade.
    Store the answers in a two-dimensional list, then write the list to the grades.txt file.
"""


def main():
    students = int(input("How many students are in your class? "))  # number of rows
    student_list = []
    line = []
    for student in range(students):
        name = input("Enter the name of the student: ")
        grade = input("Enter the letter grade for the student: ")
        line.append(name)
        line.append(grade)
        student_list.append(line)
        line = []
    print(student_list)
    file = open('grades.txt', 'w')
    for line in student_list:
        lines = f"'{line[0]}', '{line[1]}'\n"
        file.writelines(lines)
    file.close()


main()
