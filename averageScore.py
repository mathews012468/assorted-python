import csv

PATH1 = "section1_data.csv"
PATH2 = "section2_data.csv"

#Section
#First Name
#Last Name
#Unit 1 (C)
#Unit 2 (C)
#Unit 3 (C)
#Pre (C)
#Post (C)
#Change

def getAverage(file, field):
    sum = 0
    numStudents = 0
    with open(file) as f:
        scoreReader = csv.DictReader(f)
        for student in scoreReader:
            print(student["First Name"], student[field])
            sum += int(student[field])
            numStudents += 1
    average = sum/numStudents
    return average

fieldnames = ['Section', 'First Name', 'Last Name', 'Email', 'Unit 1', 'Unit 2', 'Unit 3', 'Pre', 'Post', 'Complete', 'Unit 1 (C)', 'Unit 2 (C)', 'Unit 3 (C)', 'Pre (C)', 'Post (C)', 'Change', 'Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6', 'Class 7', 'Class 8', 'Class 9', 'Class 10', 'Class 11', 'Class 12', 'Class 13', 'Class 14', 'Class 15', 'Class 16', 'Class 17', 'Class 18', 'Class 19', 'Class 20', 'Class 21', 'Class 22', 'Class 23', 'Class 24', 'Class 25', 'Class 26', 'Class 27', 'Class 28']
fields = ["Unit 1 (C)", "Unit 2 (C)", "Unit 3 (C)", "Pre (C)", "Post (C)", "Change"]
with open("average_scores_1.csv", "w") as f, open("average_scores_2.csv", "w") as g:
    scoreWriter1 = csv.DictWriter(f, fieldnames=["Field", "Average"])
    scoreWriter2 = csv.DictWriter(g, fieldnames=["Field", "Average"])
    scoreWriter1.writeheader()
    scoreWriter2.writeheader()

    for field in fields:
        scoreWriter1.writerow({"Field": field, "Average": getAverage(PATH1, field)})
        scoreWriter2.writerow({"Field": field, "Average": getAverage(PATH2, field)})
