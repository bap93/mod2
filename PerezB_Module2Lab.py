# Brooke Perez
# Case study if, else and while: Dean's List or Honor Roll
# This application asks the user for input of both name and GPA for a student.
# The application will then test if the student qualifies for either the Dean's List or Honor Roll.
# Output will include a message specifying if the student is on the Deans List, Honor Roll or does not qualify for either. 

deansList = 3.5
honorRoll = 3.25
student = None 
gpa = 0.0

DEAN_MESSAGE = "{student} qualifies for the Dean's List."
HONOR_MESSAGE = "{student} qualifies for the Honor Roll"
UNQUALIFIED_MESSAGE = "{student} does not qualify for the Dean's List or the Honor Roll"
INPUT_NAME_MESSAGE = "Please enter the student's name or zzz to quit: "
INPUT_GPA_MESSAGE = "Please enter the student's GPA: "

# loop and get name and gpa and evaulate
while True: 
    
    # get student name input
    student = input(INPUT_NAME_MESSAGE) 
    # check to see if name for student entered
    if not student: 
        print("You must enter name for the student, try again.")
        continue

    # check to see if user wants to quit
    if student.lower() == "zzz": 
        break 
    
    # get the gpa input, cast to float, retrieve input again if exception is thrown while trying to cast to float
    gpa = input(INPUT_GPA_MESSAGE) 
    try: 
        gpa = float(gpa)
    except Exception:
        print(f"Input '{gpa}' is not a float, please enter a float number") 
        continue 
    
    # check out if the student made the deans list or honor roll
    if gpa >= deansList: 
        print(DEAN_MESSAGE.format(student = student))
    elif gpa >= honorRoll: 
        print(HONOR_MESSAGE.format(student = student))
    else: 
        print(UNQUALIFIED_MESSAGE.format(student = student))
