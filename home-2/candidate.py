from question import Question
import os
import exam
class Candidate:
    def __init__(self, sid, name, time):
        self.sid = sid
        self.name = name
        self.extra_time = time
        self.exam = None
        self.confirm_details = False
        self.results = []

    def get_duration(self):
        '''
        Returns total duration of exam.
        '''
        total_duration = self.extra_time + self.exam.duration 
        return total_duration
            
    def edit_sid(self, sid):
        '''
        Update attribute sid
        '''
        positive = False
        nine_digit = False
        is_str = False 

        try:
            if isinstance(sid, str): 
                is_str = True
            if int(sid) > 0: 
                positive = True
            if len(sid) == 9: 
                nine_digit = True
            if positive and nine_digit and is_str:
                self.sid = sid
            return self.sid
        except: pass

    def edit_extra_time(self, t):
        '''
        Update attribute extra_time
        '''
        if isinstance(t, int) and t>= 0:
            self.extra_time = t
    
    def set_confirm_details(self, sid, name):
        '''
        Update attribute confim_details
        '''
        if sid == self.sid and name == self.name:
            self.confirm_details = True
            return True
        else: return False

    def log_attempt(self, data):
        '''
        Save data into candidate's file in Submissions.
        '''
        try:
            path = self.exam.path_to_dir
            absolute_path = os.path.join(path, "submissions")
            with open(f"{absolute_path}/{self.sid}.txt","w") as fobj:  
                fobj.write(data)  
              
        except FileNotFoundError:
            path = self.exam.path_to_dir
            absolute_path = os.path.join(path, "submissions")
            os.mkdir(absolute_path)
            Candidate.log_attempt(self, data)


    def set_results(self, ls):
        '''
        Update attribute results if confirm_details are True
        '''
        if self.confirm_details: 
           self.results = ls

    def do_exam(self, preview = True):
        '''
        Display exam and get candidate response from terminal during the exam.
        '''
        name = f"Candidate: {self.name}({self.sid})\n"
        t = self.get_duration()
        duration = f"Exam duration: {t} minutes\n"
        duration += "You have " + str(t) + " minutes to complete the exam.\n"

        if self.exam == None:
            exam = f"Exam preview: \nNone\n"
            return None #exit the function
        
        Exam = self.exam.preview_exam().split("\n")
        question_no = 0
        new_exam = []
        i = 0
        response = ""
        score = ""

        if preview:
            while i < len(Exam):
                if Exam[i].startswith("Expected Answer:"):
                    question_no += 1
                    Exam[i] = f"Response for Question {question_no}: "
                i += 1
            Exam = "\n".join(Exam).strip()
            str_out = name + duration + Exam
            print(str_out)

        elif not preview: 
            str_out = name + duration
            str_out = str_out.rstrip("\n")
            print(str_out)
            while i < len(Exam) - 2:
                if not Exam[i].startswith("Expected Answer:"):
                    print(Exam[i])
                elif Exam[i].startswith("Expected Answer:"):
                    question_no += 1
                    ans = input(f"Response for Question {question_no}: ")
                    question = self.exam.questions[question_no - 1]
                    mark = question.mark_response(ans)
                    response = f"Response for Question {question_no}: {ans}\n"
                    score = f"You have scored {mark:.2f} marks."
                    Exam[i] = response + score
                i += 1
            
            Exam = Exam[1:]
            exam = "\n".join(Exam).strip() 
            self.log_attempt(exam)

        
       
    def __str__(self):
        name = f"Candidate: {self.name}({self.sid})\n"
        t = self.set_duration()
        duration = f"Exam duration: {t} minutes\n"
        duration += "You have " + str(t) + " minutes to complete the exam.\n"
        if self.exam == None:
            exam = f"Exam preview: \nNone\n"
        else:
            exam = self.exam.preview_exam()
        str_out = name + duration + exam
        return str_out

