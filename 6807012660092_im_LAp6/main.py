def score_to_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

def convert_scores_to_grades():
    with open("score.txt", "r") as fin, open("grade.txt", "w") as fout:
        for line in fin:
            data = line.strip().split(",")
            student_id = data[0]
            scores = list(map(int, data[1:]))
            grades = [score_to_grade(score) for score in scores]
            fout.write(f"{student_id},{','.join(grades)}\n")

if __name__ == "__main__":
    convert_scores_to_grades()