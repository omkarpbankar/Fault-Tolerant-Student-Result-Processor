from student_operations import process_students

def main():
    # Sample data with valid and invalid student records
    students_data = [
        # Valid student
        {
            'name': 'Alice',
            'roll_number': '101',
            'marks': [85, 90, 78, 92, 88]
        },
        # Valid student - passing
        {
            'name': 'Bob',
            'roll_number': '102',
            'marks': [45, 50, 42, 60, 55]
        },
        # Valid student - failing
        {
            'name': 'Charlie',
            'roll_number': '103',
            'marks': [85, 90, 35, 92, 88]
        },
        # Invalid: missing marks
        {
            'name': 'David',
            'roll_number': '104'
        },
        # Invalid: incorrect marks count
        {
            'name': 'Eve',
            'roll_number': '105',
            'marks': [80, 90, 85]
        },
        # Invalid: out of range marks
        {
            'name': 'Frank',
            'roll_number': '106',
            'marks': [80, 90, 85, 110, 75]
        },
        # Invalid: non-numeric marks
        {
            'name': 'Grace',
            'roll_number': '107',
            'marks': [80, 90, 85, 'A', 75]
        },
        # Invalid: Missing name
        {
            'roll_number': '108',
            'marks': [80, 90, 85, 88, 75]
        }
    ]

    print("Processing students...\n")
    
    # Process the students
    results = process_students(students_data)
    
    # Display successful results
    print("--- Successfully Processed Results ---")
    for result in results:
        print(f"Name: {result['name']}, Roll: {result['roll_number']}")
        print(f"Total: {result['total']}, Percentage: {result['percentage']}%")
        print(f"Grade: {result['grade']}, Status: {result['status']}")
        print("-" * 30)

    print("\nProcessing complete. Check 'student_processor.log' for any errors.")

if __name__ == "__main__":
    main()
