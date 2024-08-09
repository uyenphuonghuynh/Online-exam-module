
'''
Interface of the exam
'''

import setup
import program_one
import random
import sys
from question import Question
import exam
import candidate

def assign_exam(Exam):
    with open(Exam.path_to_dir +"/students.csv", "r") as fobj:
        candiates = setup.extract_students(fobj)
        #original = Exam.copy_exam()
        
    if len(candiates) == 0:
        print("No candidates found in the file")
        return
    print("Assigning exam to candidates...")

    with open(Exam.path_to_dir +"/questions.txt", "r") as fobj:
        questions = setup.extract_questions(fobj)
    i = 0
    while i < len(candiates):
        if Exam.shuffle:
            candiates[i].exam = Exam.copy_exam()

        else: 
            Exam.questions = questions
            candiates[i].exam = Exam
        i += 1

    print(f"Complete. Exam allocated to {len(candiates)} candidates.")
    return candiates


def main(args):
    result = program_one.main(args)
    
    if result == False: return False
    else: questions_file, students_file = result

    correct_type = program_one.parse_cmd_args(args)

    if not correct_type: 
        return False
    else: path, duration, shuffle = correct_type

    Exam = exam.Exam(duration, path, shuffle)

    new_exam, state = program_one.setup_exam(Exam)

    candidates = assign_exam(Exam)
        
    while True: 
        user = input("Enter SID to preview student's exam (-q to quit): ")

        if user.lower() == "-q": 
            return candidates
        elif user.lower() == "-a":
            i = 0
            while i < len(candidates):
                new_exam.set_questions(Exam.questions)
                candidates[i].do_exam(True)
                print("")
                i += 1

        elif not user.isdigit(): 
            print("SID is invalid.\n")
            continue

        elif len(user) != 9:
            print("SID is invalid.\n")
            continue

        else: 
            i = 0
            valid = False
            while i < len(candidates):
                if candidates[i].sid == user: 
                    candidates[i].do_exam()
                    print("")
                    valid = True
                i += 1 
            if not valid:
                print("SID not found in list of candidates.\n")
                continue


if __name__ == "__main__":
    main(sys.argv)
