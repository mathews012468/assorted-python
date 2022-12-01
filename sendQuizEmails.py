import csv
import yagmail

#the file in QUIZ_SCORES_PATH is downloaded from Google sheets (make sure to get rid of all students not in your sections)
#For the Unit 1 Quiz, the headers of that file are:
#['Timestamp', 'Email Address', 'Score', 'What is your name?', '1) What is wrong with the following code snippet?', '2) What is the output of this code?', '3) Which type of statement can more concisely replace the code on lines 3-13?', '4) Which of the following connects a variable in source code to an object in the storyboard?']

#for the unit 2 quiz, the headers:
#['Timestamp', 'Email Address', 'Score', 'What is your name?', '1) Given the code snippet below, which of the following returns a boolean value? Choose all that apply','2) Which of the following class types does not inherit from another class?','3) What is the console output of the following code snippet? (Assume print statements print on the same line)','4) Which of the following sets up elements in the user interface in a column from top to bottom or in a row from left to right?','5) What is the output of this code snippet?']

QUIZ_SCORES_PATH = "PATH TO FILE WITH QUIZ SCORES"
INSTRUCTOR_NAME = "YOUR NAME"
SENDER_EMAIL = "EMAIL YOU'RE SENDING FROM"

# the passcode below comes from an app connected to gmail, more info in the link below
# basically, you can't just enter your password when two factor authentication is enabled
# https://stackoverflow.com/questions/26736062/sending-email-fails-when-two-factor-authentication-is-on-for-gmail
PASSCODE = "CODE TO GET ACCESS TO EMAIL"
NUM_OF_QUESTIONS = 4

with open(QUIZ_SCORES_PATH) as f:
    quiz_scores_reader = csv.DictReader(f)

    right_answers = ["c) x must be initialized as a var.", "d) Code does not compile", "c) A switch statement", "d) Outlet"]

    for response in quiz_scores_reader:
        name = response["What is your name?"].title().strip()
        score = response["Score"]
        email = response["Email Address"]
        student_answers = [response["1) What is wrong with the following code snippet?"], response["2) What is the output of this code?"], response["3) Which type of statement can more concisely replace the code on lines 3-13?"], response["4) Which of the following connects a variable in source code to an object in the storyboard?"]]

        email_template = f"Hello {name},\n\nYou scored a {score} on the Unit 1 quiz.\n\n"

        for i in range(NUM_OF_QUESTIONS):
            email_template += f"You answered question {i+1} "
            if student_answers[i] == right_answers[i]:
                email_template += "correctly."
            else:
                email_template += f"incorrectly. You answered \"{student_answers[i]}\", when the right answer was \"{right_answers[i]}\"."
            email_template += "\n"
        
        email_template += f"\nBest,\n{INSTRUCTOR_NAME}"
        print(email_template)

        #uncomment the following two lines of code to send the emails
        # yag = yagmail.SMTP(SENDER_EMAIL, PASSCODE)
        # yag.send(email, subject="Quiz Scores Unit 1", contents=email_template)
