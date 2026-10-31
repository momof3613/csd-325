# Ajanae Stanback
# CSD-325 Module 2.2
# Student Grade Calculator

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
    score = float(input("Enter student score: "))
    breakpoint()
    grade = calculate_grade(score)
    print("Student grade:", grade)


if __name__ == "__main__":
    main()
