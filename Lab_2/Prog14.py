# Accept marks of three subjects. Print total and average along with whether a candidate has passed or fail.
def final_result(marks):
    total = sum(marks)
    average = total / len(marks)
    result = "Fail" if any(mark < 40 for mark in marks) else "Pass"
    
    grades = []
    for mark in marks:
        if mark == "Absent":
            grades.append("NA")
        elif mark < 40:
            grades.append("F")
        elif mark <= 44:
            grades.append("P")
        elif mark <= 49:
            grades.append("C")
        elif mark <= 54:
            grades.append("B")
        elif mark <= 59:
            grades.append("B+")
        elif mark <= 69:
            grades.append("A")
        elif mark <= 79:
            grades.append("A+")
        else:
            grades.append("O")
    
    return total, average, result, grades

marks = []
for i in range(3):
    mark = input(f"Enter marks for subject {i+1} (or type 'Absent'): ")
    marks.append(int(mark) if mark.isdigit() else "Absent")

total, average, result, grades = final_result(marks)
print(f"Total: {total}, Average: {average:.2f}, Result: {result}, Grades: {grades}")