import csv
import yagmail

#the file in QUIZ_SCORES_PATH is downloaded from Google sheets (make sure to get rid of all students not in your sections)
#For the Unit 1 Quiz, the headers of that file are:
#['Timestamp', 'Email Address', 'Score', 'What is your name?', '1) What is wrong with the following code snippet?', '2) What is the output of this code?', '3) Which type of statement can more concisely replace the code on lines 3-13?', '4) Which of the following connects a variable in source code to an object in the storyboard?']

#for the unit 2 quiz, the headers:
#['Timestamp', 'Email Address', 'Score', 'What is your name?', '1) Given the code snippet below, which of the following returns a boolean value? Choose all that apply','2) Which of the following class types does not inherit from another class?','3) What is the console output of the following code snippet? (Assume print statements print on the same line)','4) Which of the following sets up elements in the user interface in a column from top to bottom or in a row from left to right?','5) What is the output of this code snippet?']

def send_emails(unit, quiz_scores_path, instructor_name, sender_email, passcode):
    input("are you sure?")
    unit_to_questions = {
        1: ['1) What is wrong with the following code snippet?', '2) What is the output of this code?', '3) Which type of statement can more concisely replace the code on lines 3-13?', '4) Which of the following connects a variable in source code to an object in the storyboard?'],
        2: ['1) Given the code snippet below, which of the following returns a boolean value? Choose all that apply.','2) Which of the following class types does not inherit from another class?','3) What is the console output of the following code snippet? (Assume print statements print on the same line)','4) Which of the following sets up elements in the user interface in a column from top to bottom or in a row from left to right?','5) What is the output of this code snippet?']
    }
    questions = unit_to_questions[unit]

    unit_to_answers = {
        1: ["c) x must be initialized as a var.","d) Code does not compile","c) A switch statement","d) Outlet"],
        2: ["a) array.isEmpty, d) array[0]", "c) base class", "b) Hey! 4", "c) Stack View", "TRUE"]
    }
    right_answers = unit_to_answers[unit]

    subject = f"Quiz Scores Unit {unit}"
    with open(quiz_scores_path) as f:
        quiz_scores_reader = csv.DictReader(f)

        for response in quiz_scores_reader:
            name = response["What is your name?"].title().strip()
            score = response["Score"]
            email = response["Email Address"]
            student_answers = [response[question] for question in questions]

            email_template = f"Hello {name},\n\nYou scored a {score} on the Unit {UNIT} quiz.\n\n"

            for i in range(len(questions)):
                email_template += f"You answered question {i+1} "
                if student_answers[i].lower() == right_answers[i].lower():
                    email_template += "correctly."
                else:
                    email_template += f"incorrectly. You answered \"{student_answers[i]}\", when the right answer was \"{right_answers[i]}\"."
                email_template += "\n"
                
            email_template += f"\nBest,\n{instructor_name}"
            print(email_template)

            print(subject)
            # uncomment the following two lines of code to send the emails
            # yag = yagmail.SMTP(sender_email, passcode)
            # yag.send(email, subject=f"Quiz Scores Unit {unit}", contents=email_template)


#"/Users/mathewsoto/Downloads/Unit 1 Quiz (Responses) - Form Responses 1.csv"
#/Users/mathewsoto/Downloads/Unit 2 Quiz Section 1 (Responses) - Form Responses 1.csv
UNIT = 2
QUIZ_SCORES_PATH = "/Users/mathewsoto/Downloads/Unit 2 Quiz Section 1 (Responses) - Form Responses 1.csv"
INSTRUCTOR_NAME = "Mathew Soto"
SENDER_EMAIL = "mathewsoto@nypl.org"

# the passcode below comes from an app connected to gmail, more info in the link below
# basically, you can't just enter your password when two factor authentication is enabled
# https://stackoverflow.com/questions/26736062/sending-email-fails-when-two-factor-authentication-is-on-for-gmail
PASSCODE = "pvdafwnziedvpien"

send_emails(UNIT, QUIZ_SCORES_PATH, INSTRUCTOR_NAME, SENDER_EMAIL, PASSCODE)