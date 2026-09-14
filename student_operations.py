from exceptions import InvalidMarksError, InvalidStudentDataError
from logger import get_logger
from result_calculator import calculate_total, calculate_percentage, determine_grade, determine_pass_fail

logger = get_logger()

def validate_student_data(student):
    """Validates if student details are present."""
    if 'name' not in student or not student['name']:
        raise InvalidStudentDataError("Student name is missing or empty.")
    if 'roll_number' not in student or not student['roll_number']:
        raise InvalidStudentDataError(f"Roll number is missing for student: {student.get('name', 'Unknown')}.")
    if 'marks' not in student:
        raise InvalidStudentDataError(f"Marks are missing for student: {student['name']}.")

def validate_marks(marks):
    """Validates the list of marks."""
    if not isinstance(marks, list):
        raise TypeError("Marks must be provided as a list.")
    
    if len(marks) != 5:
        raise ValueError(f"Expected 5 subjects, got {len(marks)}")
        
    valid_marks = []
    for mark in marks:
        if not isinstance(mark, (int, float)):
            raise InvalidMarksError(f"Mark '{mark}' is not a numeric value.")
        if mark < 0 or mark > 100:
            raise InvalidMarksError(f"Mark '{mark}' is out of range 0-100.")
        valid_marks.append(float(mark))
    
    return valid_marks

def process_students(students_data):
    """Processes a list of students, calculating results and handling errors."""
    processed_results = []
    
    for student in students_data:
        try:
            # 1. Validate student information
            validate_student_data(student)
            
            # 2. Validate marks
            valid_marks = validate_marks(student['marks'])
            
            # 3. Calculate Results
            total = calculate_total(valid_marks)
            percentage = calculate_percentage(valid_marks)
            grade = determine_grade(percentage)
            status = determine_pass_fail(valid_marks)
            
            # 4. Store successful result
            result = {
                'name': student['name'],
                'roll_number': student['roll_number'],
                'total': total,
                'percentage': round(percentage, 2),
                'grade': grade,
                'status': status
            }
            processed_results.append(result)
            
        except (InvalidStudentDataError, InvalidMarksError, TypeError, ValueError, ZeroDivisionError) as e:
            # Log the error and continue to the next student
            student_identifier = student.get('name') or student.get('roll_number') or 'Unknown'
            logger.error(f"Error processing student '{student_identifier}': {e}")
            continue
        except Exception as e:
            # Catch-all for unexpected errors
            student_identifier = student.get('name') or student.get('roll_number') or 'Unknown'
            logger.error(f"Unexpected error processing student '{student_identifier}': {e}")
            continue
            
    return processed_results
