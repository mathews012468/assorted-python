import csv

PATH = "/Users/mathewsoto/Downloads/FY22 SWFT Attendance Sheets - Assessments (Complete Data Only).csv"
with open(PATH) as f:
    csvReader = csv.DictReader(f)
    #Section
    #First Name
    #Last Name
    #Unit 1 (C)
    #Unit 2 (C)
    #Unit 3 (C)
    #Pre (C)
    #Post (C)
    #Change
    
    section1 = []
    section2 = []
    for record in csvReader:
        if record["Section"] == "1":
            section1.append(record)
        else:
            section2.append(record)

fieldnames = ['Section', 'First Name', 'Last Name', 'Email', 'Unit 1', 'Unit 2', 'Unit 3', 'Pre', 'Post', 'Complete', 'Unit 1 (C)', 'Unit 2 (C)', 'Unit 3 (C)', 'Pre (C)', 'Post (C)', 'Change', 'Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6', 'Class 7', 'Class 8', 'Class 9', 'Class 10', 'Class 11', 'Class 12', 'Class 13', 'Class 14', 'Class 15', 'Class 16', 'Class 17', 'Class 18', 'Class 19', 'Class 20', 'Class 21', 'Class 22', 'Class 23', 'Class 24', 'Class 25', 'Class 26', 'Class 27', 'Class 28']
with open("section1_data.csv", "w") as f, open("section2_data.csv", "w") as g:
    section1_writer = csv.DictWriter(f, fieldnames=fieldnames)
    section1_writer.writeheader()
    for record in section1:
        section1_writer.writerow(record)
    
    section2_writer = csv.DictWriter(g, fieldnames=fieldnames)
    section2_writer.writeheader()
    for record in section2:
        section2_writer.writerow(record)
