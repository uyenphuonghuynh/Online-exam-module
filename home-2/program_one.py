'''
Interface of the exam
'''

import setup
import sys
import os
from exam import Exam

def parse_cmd_args(args):
    '''
    Parameters:
        args: list, command line arguments
    Returns:
        result: None|tuple, details of the exam

    >>> parse_cmd_args(['program.py', '/home/info1110/', '60', '-r'])
    ('/home/info1110/', 60, True)

    >>> parse_cmd_args(['program.py', '/home/info1110/', 'ab', '-r'])
    Duration must be an integer

    >>> parse_cmd_args(['program.py', '/home/info1110/'])
    Check command line arguments
    '''
    try:
        shuffle = False

        if len(args) < 3:
            raise ValueError("Check command line arguments")
        
        if not args[2].isdigit():
            raise TypeError("Duration must be an integer")

        duration = int(args[2])

        if len(args) >= 4 and args[3] == "-r":
            shuffle = True
        
        tuple = (args[1], duration, shuffle)
        return tuple

    except ValueError as ve:
        print(ve)
        return None
    except TypeError as te:
        print(te)
        return None
    

    
def setup_exam(obj):
    '''
    Update exam object with question contents extracted from file 
    Parameter:
        obj: Exam object
    Returns:
        (obj, status): tuple containing updated Exam object and status
        where status: bool, True if exam is setup successfully. Otherwise, False.
    '''
    with open(obj.path_to_dir + "/questions.txt", "r") as fobj:

        question_ls = setup.extract_questions(fobj)  
        obj.set_questions(question_ls) 
        obj.set_exam_status()

        return (obj, obj.exam_status)



def main(args):
    '''
    Implement all stages of exam process.
    '''

    correct_type = parse_cmd_args(args)

    if not correct_type: 
        return False
    else: path, duration, shuffle = correct_type

    questions_file = os.path.join(path, "questions.txt")
    students_file = os.path.join(path, "students.csv")


    if not (os.path.isfile(questions_file) and os.path.isfile(students_file)):
        print("Missing files")
        return False

    print("Setting up exam...")

    obj = Exam(duration, path, shuffle)
    
    exam, status = setup_exam(obj)

    if status:
        print("Exam is ready...")
    else:
        print("Error setting up exam")
        return False 

    while True:
        review = input("Do you want to preview the exam [Y|N]? ")
        if review.lower() != "n" and review.lower() != "y": 
            print("Invalid command.")
    
        elif review.lower() == "n": 
            return questions_file, students_file

        elif review.lower() == "y": 
            ques_format = exam.set_questions(exam.questions)
            preview = exam.preview_exam().rstrip("\n") + "\n"
            print(preview)

        
    
if __name__ == "__main__":
    '''
    DO NOT REMOVE
    '''
    main(sys.argv)
