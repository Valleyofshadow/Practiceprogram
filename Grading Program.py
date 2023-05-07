student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Nevill" : 62
}
for key in student_scores:
    if student_scores[key] <= 70 and student_scores[key] >= 0:
        print (key, ": Fail")
    elif student_scores[key] >= 71 and student_scores [key] <= 80:
        print(key, ": Acceptable")
    elif student_scores[key] >= 81 and student_scores [key] <= 90:
        print(key, ": Exceeds Expectations")
    elif student_scores[key] >= 91 and student_scores [key] <= 100:
        print (key, ": Outstanding")
    else:
        print (key, ": Grade outside of limits")