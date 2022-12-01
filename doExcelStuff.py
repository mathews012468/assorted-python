import csv

PATH_TO_ATTENDANCE_1 = "/Users/mathewsoto/Documents/ZoomAttendance/participants_01032022_fopwpp1.csv"
PATH_TO_ATTENDANCE_2 = "/Users/mathewsoto/Documents/ZoomAttendance/participants_01032022_fopwpp2.csv"

PATH_TO_REGISTRATIONS_1 = "/Users/mathewsoto/Downloads/registrations.csv"
PATH_TO_REGISTRATIONS_2 = "/Users/mathewsoto/Downloads/registrations (1).csv"

def hasNcharsInCommon(firstWord, secondWord, n):
    fourLetterSubstringsFirstWord = {firstWord[i:i+4] for i in range(len(firstWord)-3)} 
    fourLetterSubstringsSecondWord = {secondWord[i:i+4] for i in range(len(secondWord)-3)}
    if fourLetterSubstringsFirstWord & fourLetterSubstringsSecondWord:
        return True
    return False

def getEntryByName(name):
    #if name has a run of at least four characters in common with a name in the registrations,
    #consider it the same name and return that entry
    with open(PATH_TO_REGISTRATIONS_1) as f, open(PATH_TO_REGISTRATIONS_2) as g:
        registrationsReader1 = csv.DictReader(f)
        registrationsReader2 = csv.DictReader(g)

        for student in registrationsReader1:
            if hasNcharsInCommon(student["Name"].lower(), name.lower(), 4):
                return student, name
        for student in registrationsReader2:
            if hasNcharsInCommon(student["Name"].lower(), name.lower(), 4):
                return student, name
    return None, name

with open("fileFun/namesrevised.txt") as f, open("fileFun/namesAndEmails.csv", "w") as g:
    studentWriter = csv.DictWriter(g, fieldnames=['Name', 'Phone', 'E-mail', 'State', 'Attended?', 'Date Registered', 'Library Barcode'])
    studentWriter.writeheader()
    for name in f:
        name = name.strip()
        entry = getEntryByName(name)
        if entry[0] != None:
            studentWriter.writerow(entry[0])
        else:
            print(entry[1])

# with open(PATH_TO_ATTENDANCE_1) as f, open(PATH_TO_ATTENDANCE_2) as g:
#     f.readline() #skip nonsense title
#     g.readline() #skip nonsense title

#     attendanceReader1 = csv.DictReader(f)
#     attendanceReader2 = csv.DictReader(g)

#     uniqueNames1 = {student['Name (Original Name)'] for student in attendanceReader1}
#     uniqueNames2 = {student['Name (Original Name)'] for student in attendanceReader2}
#     uniqueNames1.discard("Mathew Soto")
#     uniqueNames2.discard("Mathew Soto")

#     # with open("fileFun/names1.txt", "w") as h:
#     #     for name in uniqueNames1:
#     #         h.write(name + "\n")
#     # with open("fileFun/names2.txt", "w") as h:
#     #     for name in uniqueNames2:
#     #         h.write(name + "\n")
    
#     uniqueNames = uniqueNames1 | uniqueNames2
#     # with open("fileFun/names.txt", "w") as h:
#     #     for name in uniqueNames:
#     #         h.write(name + "\n")
#     print(len(uniqueNames1), len(uniqueNames2), len(uniqueNames))
    
#Eltrapcollection
#Emma
#p
#rita_