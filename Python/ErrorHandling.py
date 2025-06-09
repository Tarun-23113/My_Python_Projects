def calculate_grade(score):
    grade = None
    try:
        if (score < 0 or score > 100):
            raise ValueError("Enter a Value between 0 - 100")
        else:
            if score < 20:
                grade = 'C'
            elif score < 40:
                grade = 'B'
            elif score < 60:
                grade = 'A'
            else:
                grade = 'E'
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Wrong Type: {e}")
    else:
        print(f"Grade Calculated Successfully {grade}")
    finally:
        print("Grading Process Finished")

calculate_grade(90)