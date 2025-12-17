import random

def generate_scores():
    with open("score.txt", "w") as f:
        for student_id in range(1000, 1100):  # 100 students
            english = random.randint(50, 100)
            math = random.randint(50, 100)
            programming = random.randint(50, 100)
            ai = random.randint(50, 100)
            db = random.randint(50, 100)
            f.write(f"{student_id},{english},{math},{programming},{ai},{db}\n")

if __name__ == "__main__":
    generate_scores()