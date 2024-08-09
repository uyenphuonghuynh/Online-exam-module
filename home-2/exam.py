import os
from question import Question
class Exam:
    def __init__(self, duration, path, shuffle):
        self.duration = duration
        self.path_to_dir = path
        self.shuffle = shuffle
        self.exam_status = False
        self.questions = []
        self.set_name(path)


    def set_name(self, path):
        """
        Sets the name of the exam. 
        """
        # you'll need to add some code here
        path_list = path.split("/")
        dirname = path_list[-1]
        dirname = dirname.replace(" ","_")
        self.name = dirname

    def get_name(self):
        """
        Returns formatted string of exam name.
        """
        self.name = self.name.replace("_"," ")
        self.name = self.name.upper()
        return self.name
    
    def set_exam_status(self):
        '''
        Set exam_status to True only if exam has questions.
        '''
        if len(self.questions) != 0:
            self.exam_status = True
        
    
    def set_duration(self, t):
        '''
        Update duration of exam.
        Parameter:
            t: int, new duration of exam.
        '''
        if t > 0:
            self.duration = t

    def set_questions(self, ls):
        '''
        Verifies all questions in the exam are complete.
        Parameter:
            ls: list, list of Question objects
        Returns:
            status: bool, True if set successfully.
        '''
        ques_no = 0
        if isinstance(ls, list) == False:
            return False
         
        while ques_no < len(ls):
            question = ls[ques_no]
            if question.qtype != "end":
                if question.description == None or question.correct_answer == None:
                    print("Description or correct answer missing") 
                    return False

                elif question.qtype == "single" or question.qtype == "multiple":
                    if not question.answer_options or len(question.answer_options) != 4: 
                        print("Answer options incorrect quantity")
                        return False

                elif question.qtype == "short":
                    if question.answer_options:
                        print("Answer options should not exist")
                        return False
            

            elif question.qtype == "end" and ls[ques_no].description != None:
                    print("End marker missing or invalid")
                    return False
            
            ques_no += 1

        if ls[-1].qtype != "end":
            print("End marker missing or invalid")
            return False
            
        self.questions = ls
        return True


    def preview_exam(self):
        '''
        Returns a formatted string.
        '''
        no_ques = 0
        preview_q_str = self.name.upper().replace("_"," ") + "\n"
        while no_ques < len(self.questions):
            no_ques += 1
            question = self.questions[(no_ques - 1)]
            preview_q_str += str(question.preview_question(no_ques)) + "\n"
            preview_q_str += "\n"
        return preview_q_str
    
    def copy_exam(self):
        '''
        Create a new exam object using the values of this instances' values.
        '''
        # TODO: make a new exam object (call the constructor)
        exam = Exam(self.duration, self.path_to_dir, self.shuffle)

        # make a new list of questions to reassign to the attribute
        questions = self.questions
        ls = []
        i = 0
        while i < len(questions):
            # call the copy method for this question
            # TODO: (you'll need to write this instance method in Question)
            new_question = questions[i].copy_question()
            new_question.shuffle_answers()

            # insert this into new list of questions
            ls.append(new_question)
            
            i += 1

        # TODO: assign this new question list to the new exam
        exam.questions = ls
        
        # return the new exam
        return exam

    def __str__(self):
        pass
