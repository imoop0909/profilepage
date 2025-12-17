def get_grade(average_score):
    """
    Determines the letter grade based on the average score.

    Args:
        average_score (float): The average score of a student.

    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if average_score >= 80:
        return 'A'
    elif average_score >= 70:
        return 'B'
    elif average_score >= 60:
        return 'C'
    elif average_score >= 50:
        return 'D'
    else:
        return 'F'

def analyze_student_data(students_data):
    """
    Analyzes raw student score data to compute total scores and letter grades.

    Args:
        students_data (dict): A dictionary of student scores.

    Returns:
        dict: A new dictionary with calculated totals and grades for each student.
    """
    analyzed_data = {}
    
    for student_id, scores in students_data.items():
        total_score = sum(scores.values())
        average_score = total_score / len(scores)
        letter_grade = get_grade(average_score)
        
        analyzed_data[student_id] = {
            "Total": total_score,
            "Average": round(average_score, 2),
            "Grade": letter_grade
        }
    
    return analyzed_data
