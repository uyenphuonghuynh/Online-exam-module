'''
Operate by writing in the terminal "python test_program.py"
'''
from question import Question
def one(arg):
    assert Question.mark_response(arg, "Bob") == 1, "Correct answer isn't marked correctly"
    print("Test 01 is successful")

def two(arg):
    assert Question.mark_response(arg, "BOB") == 0, "Incorrect answer is marked incorrectly"
    print("Test 02 is successful")

def three(arg):
    assert Question.mark_response(arg, "D") == 1, "Correct answer is marked incorrectly"
    print("Test 03 is successful") 

def four(arg):
    assert Question.mark_response(arg, "B") == 0, "Incorrect answer is marked incorrectly"
    print("Test 04 is successful")


def five(arg):
    assert Question.mark_response(arg, "A, B, C") == 2, "Correct answer(s) is marked incorrectly"
    print("Test 05 is successful")

def six(arg):
    assert Question.mark_response(arg, "A, D") == 1, "Incorrect answer(s) is marked incorrectly"
    print("Test 06 is successful")


    
arg = Question("short")
arg.set_correct_answer("Bob")
arg.set_marks(1)
one(arg)
two(arg)

arg = Question("single")
arg.set_correct_answer("D")
arg.set_marks(1)
three(arg)
four(arg)

arg = Question("multiple")
arg.set_correct_answer("A, B")
arg.set_marks(2)
five(arg)
six(arg)


