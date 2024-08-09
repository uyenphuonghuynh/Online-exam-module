'''
Functions to setup the exam questions and candidate list for the exam.
'''
# please do not change or add another import
import question
import candidate
import io
import random

def extract_questions(fobj: io.TextIOWrapper)->list:
    """
    Parses fobj to extract details of each question found in the file.
    General procedure to extract question.
    1. Extract the following
        - type
        - question details (description)
        - possible answers (if any)
        - expected answer
        - marks
        (you shouldn't need to perform error handling on these details,
        this is handled in the next step).
    2. You'll need to convert the possible answers (if any) to a list of tuples (see 
       "Section 1. Setup the exam - Question" for more details). All flags can be False.
    3. Create a question object and call the instance methods to set the
       attributes. This will handle the error handling.
    4. Repeat Steps 1-3 for the next question until there are no more questions.
    5. You will need to create an end question as well.
    6. Create the list for all your questions and return it.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Question objects.
    """

    fobj = "".join(fobj.readlines())
    question_ls = fobj.split("\n\n")
    i = 0
    result = []
    
    while i < len(question_ls):

        ques_no = question_ls[i].split("\n")
        qtype_ls = ques_no[0].split("- ")
        qtype = qtype_ls[1].strip("\n")
        ques_content = question.Question(qtype.lower())

        j = 1
        possible_ans = 0
        expected_ans = 0
        description = ""

        while j < len(ques_no):
            if ques_no[j].startswith("Possible Answers:"):
                possible_ans = j
                break
            elif ques_no[j].startswith("Expected Answer:"):
                expected_ans = j
                break
            description += ques_no[j] + "\n"
            j += 1

        description = description.rstrip("\n")
        ques_content.set_description(description)

        option_ls = []
        if (possible_ans):
            possible_ans += 1
            while possible_ans < len(ques_no):

                if ques_no[possible_ans].startswith("Expected Answer:"):
                    expected_ans = possible_ans
                    break

                option = (ques_no[possible_ans], False)
                option_ls.append(option)
                possible_ans += 1
        try:
            correct_ans = str(ques_no[expected_ans].split(": ")[1])
            ques_content.set_correct_answer(correct_ans)
        except: pass

        ques_content.set_answer_options(option_ls)
        score = expected_ans + 1
        while score < len(ques_no):
            if ques_no[score].startswith("Marks: "):
                mark = ques_no[score].split(": ")[1]
                mark = int(mark)
            score += 1
        ques_content.set_marks(mark)

        result.append(ques_content)
        i += 1
    
    result.append(question.Question("end"))

    return result


def sort(to_sort: list, order: int=0)->list:
    """
    Sorts to_sort depending on settings of order.

    Parameters:
        to_sort: list, list to be sorted.
        order: int, 0 - no sort, 1 - ascending, 2 - descending
    Returns
        result: list, sorted results.

    Sample usage:
    >>> to_sort = [(1.50, "orange"), (1.02, "apples"), (10.40, "strawberries")]
    >>> print("Sort 0:", sort(to_sort, 0))
    Sort 0: [(1.5, 'orange'), (1.02, 'apples'), (10.4, 'strawberries')]
    >>> print("Sort 1:", sort(to_sort, 1))
    Sort 1: [(1.02, 'apples'), (1.5, 'orange'), (10.4, 'strawberries')]
    >>> print("Sort 2:", sort(to_sort, 2))
    Sort 2: [(10.4, 'strawberries'), (1.5, 'orange'), (1.02, 'apples')]
    >>> to_sort = [ "oranges", "apples", "strawberries"]
    >>> print("Sort 0:", sort(to_sort, 0))
    Sort 0: ['oranges', 'apples', 'strawberries']
    >>> print("Sort 1:", sort(to_sort, 1))
    Sort 1: ['apples', 'oranges', 'strawberries']
    >>> print("Sort 2:", sort(to_sort, 2))
    Sort 2: ['strawberries', 'oranges', 'apples']
    """
    if not isinstance(to_sort, list): 
        return to_sort
    
    if order == 0 or order >2: 
        return to_sort 

    elif order == 1:
        i = 0
        while i < len(to_sort):
            j = 0
            while j < (len(to_sort) - i - 1): # (n-i-1) is the new list that we loops through (its getting smaller)
                if to_sort[j] > to_sort[j+1]: #swap the element location if the element before is bigger than the element follows it
                    to_sort[j], to_sort[j+1] =  to_sort[j+1], to_sort[j] 
                j += 1
            i += 1 
        return to_sort
    
    elif order == 2:
        to_sort = sort(to_sort, 1)
        new_ls = []
        i = 0
        while i < len(to_sort):
            i += 1
            new_ls.append(to_sort[-i])
        return new_ls


def extract_students(fobj: io.TextIOWrapper)->list:
    """
    Parses fobj to extract details of each student found in the file.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Candidate objects sorted in ascending order
    """
    try:
        content = fobj.readlines()
        i = 1
        ls = []

        while i < len(content):
            student_info = content[i].rstrip("\n").split(",")
            sid = student_info[0]
            name = student_info[1]

            if student_info[2].isdigit():
                time = int(student_info[2])
            else: time = 0

            ls.append((sid, name, time))
            i += 1

        ls = sort(ls, 1)
        i = 0
        result = []
        while i < len(ls):
            sid, name, time = ls[i]
            obj = candidate.Candidate(sid, name, time)
            i += 1
            result.append(obj)

        return result
       
    except Exception: return []




