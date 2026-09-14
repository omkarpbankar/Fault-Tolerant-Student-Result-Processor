# Fault-Tolerant Student Result Processor

## Project Overview

This is a Python-based student result processor designed to demonstrate robust error handling and fault tolerance. The program processes a batch of student records containing their basic details and marks across 5 subjects. It calculates the total marks, percentage, grade, and pass/fail status for each student.

A key feature of this processor is its fault tolerance. In real-world data processing, inputs are often messy. Instead of terminating execution when encountering invalid data, the application uses custom exceptions, traps the errors, logs them appropriately, and safely continues processing the remaining student records.

### Key Features
- **Calculates Results:** Determines total, percentage, grade (A, B, C, D, F), and pass/fail status.
- **Fault-Tolerant:** Safely skips over invalid student records (e.g., missing data, non-numeric marks) without crashing.
- **Custom Exceptions:** Uses `InvalidMarksError` and `InvalidStudentDataError` to provide clear, specific error context.
- **Logging:** Errors are recorded both to the console and a `student_processor.log` file, aiding debugging without disrupting output.
- **Modular Design:** Separation of concerns across `exceptions.py`, `logger.py`, `result_calculator.py`, and `student_operations.py`.

## How to Run

1. Ensure you have Python installed.
2. Navigate to the project directory.
3. Run the main script:

```bash
python main.py
```

Check the console output for successfully processed students and review `student_processor.log` for any data validation errors that occurred during processing.