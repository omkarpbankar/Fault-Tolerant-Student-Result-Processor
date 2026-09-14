def calculate_total(marks):
    """Calculates the total of marks."""
    return sum(marks)

def calculate_percentage(marks):
    """Calculates the percentage based on marks out of 100."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)

def determine_grade(percentage):
    """Determines the grade based on percentage."""
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'

def determine_pass_fail(marks):
    """Determines pass or fail based on passing criteria. 
    Assumes passing marks is 40 for each subject."""
    for mark in marks:
        if mark < 40:
            return 'Fail'
    return 'Pass'
