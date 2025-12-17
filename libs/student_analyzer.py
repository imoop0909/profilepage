import random

def generate_student_scores(num_students):
    """
    Generates a dictionary of random scores for a specified number of students.

    Args:
        num_students (int): The number of students to generate data for.

    Returns:
        dict: A dictionary where keys are student IDs (e.g., 'S001') and
              values are dictionaries containing scores for each subject.
    """
    students_data = {}
    subjects = ["English", "Programming", "Networking", "Mathematics"]
    
    for i in range(1, num_students + 1):
        student_id = f"S{i:03d}"
        scores = {subject: random.randint(0, 100) for subject in subjects}
        students_data[student_id] = scores
        
    return students_data