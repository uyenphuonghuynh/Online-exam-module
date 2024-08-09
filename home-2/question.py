import random
class Question:

    def __init__(self, qtype):
        # you'll need to check if qtype is valid before assigning it    
        if qtype == "single" or qtype == "multiple" or qtype == "short" or qtype == "end":
            self.qtype = qtype
        else: 
            self.qtype = None
        self.description = None
        self.answer_options = []
        self.correct_answer = None
        self.marks = None
       
    def set_type(self, qtype):
        """
        Update instance variable qtype.
        """
        valid_qtype = ["single", "multiple", "short", "end"]
        i = 0
        result = False
        while i < len(valid_qtype):
            if qtype == valid_qtype[i]: 
                self.qtype = qtype
                result = True
            i += 1
        if result == False:
           self.qtype = None
        return result

    def set_description(self, desc):
        """
        Update instance variable description.
        """
        if self.qtype == "end":
            return False
        if type(desc) == str and desc != "":
            self.description = desc
            return True
        else: return False
        
    def set_correct_answer(self, ans):
        """
        Update instance variable correct_answer.
        """
        result = False
        #list of answers option:
        ls_option = ["A", "B", "C", "D"]
        i = 0
        x = 0 #to go through the multiple answers
        #count elements(answer) in multiple choice answers
        ele = 0

        if self.qtype == "end":
            return False
        
        elif type(ans) == str:
            if self.qtype == "single":
                 while i < len(ls_option):
                    if ans == ls_option[i]:
                         self.correct_answer = ans
                         result = True
                    i += 1

            if self.qtype == "multiple":
                #comma separated string of option values (e.g. A, B, C).
                ans_list = ans.split(", ")
                while i < len(ans_list):
                    while x < len(ls_option):
                        if ans_list[i] == ls_option[x]:
                            ele += 1
                        x += 1
                    i += 1
                if (ele): #to make sure there is 1 or more correct answers for multiple choice question
                    self.correct_answer = ans
                    result = True

            elif self.qtype == "short":
                self.correct_answer = ans
                result = True
                
        return result

    def set_marks(self, num):
        """
        Update instance variable marks.
        """
        if self.qtype == "end":
            return False
        if isinstance(num, int) == True and num >= 0:
            self.marks = num
            return True
        else: return False

    
    def set_answer_options(self, opts):
        """
        Update instance variable answer_options.
        opts should have all flags equal to False when passed in.
        This method will update the flags based on the correct answer.
        Only then do we check that the number of correct answers is correct.
        """
        two_ele_tuple = False
        ans_des_star = False
        is_list = False
        ans_format = False
        correct_ans = False
        count_correct_conditions = 0
        if len(opts) ==4: 
            ans_des1 = opts[0][0]
            ans_des2 = opts[1][0]
            ans_des3 = opts[2][0]
            ans_des4 = opts[3][0]
            ans_des = [ans_des1, ans_des2,  ans_des3,  ans_des4]
        else: return False 

        if self.qtype == "short" or self.qtype == "end":
            self.answer_options = opts
            return True
        
        else:
            if isinstance(opts, list):
                is_list = True
                count_correct_conditions += 1
            else: 
                return False

            if len(opts[0]) == 2 and len(opts[1]) == 2 and len(opts[2]) == 2 and len(opts[3]) == 2:
                two_ele_tuple = True
                count_correct_conditions += 1
            else: 
                return False
            
            if ans_des[0].startswith("A.") and ans_des[1].startswith("B.") and ans_des[2].startswith("C.") and ans_des[3].startswith("D."):
                ans_format = True
                count_correct_conditions += 1
            else: 
                return False
            
            if isinstance(ans_des1,str) and isinstance(ans_des2,str) and isinstance(ans_des3,str) and isinstance(ans_des4,str):
                is_string = True
                count_correct_conditions +=1
            else: 
                return False
            
            valid_ans = ["A", "B", "C", "D"]

            count_correct_ans = 0
            if self.qtype == "single":
                i = 0
                while i < len(valid_ans):
                    if self.correct_answer == valid_ans[i]:
                        opts[i] = (opts[i][0], True)
                        count_correct_ans += 1
                    i += 1
            
            elif self.qtype == "multiple":
                correct_answer = self.correct_answer.split(", ")
                loop_tho_valid_ans = 0
                loop_tho_correct_answer = 0

                while loop_tho_valid_ans < len(valid_ans):
                    while loop_tho_correct_answer < len(correct_answer):
                        if correct_answer[loop_tho_correct_answer] == valid_ans[loop_tho_valid_ans]:
                            opts[loop_tho_valid_ans] = (opts[loop_tho_valid_ans][0], True)
                            count_correct_ans += 1
                            break
                        loop_tho_correct_answer += 1
                    loop_tho_correct_answer = 0
                    loop_tho_valid_ans += 1
                    

            if self.qtype == "single" and count_correct_ans == 1: 
                correct_ans = True
                self.answer_options = opts
                count_correct_conditions +=1
                return True
            elif self.qtype == "multiple" and count_correct_ans >= 1: 
                correct_ans = True
                self.answer_options = opts
                count_correct_conditions +=1
                return True
            else: return False
            

                    
    def get_answer_option_descriptions(self):
        """
        Returns formatted string listing each answer description on a new line.
        Example:
        A. Answer description
        B. Answer description
        C. Answer description
        D. Answer description
        """
        if self.qtype == "short" or self.qtype == "end": 
            return ""
        if self.qtype == "single" or self.qtype == "multiple":
            ans_opt = 0
            result = ""
            while ans_opt < len(self.answer_options):
                result += str(self.answer_options[ans_opt][0])
                if ans_opt != len(self.answer_options) - 1 : 
                    result += "\n"
                ans_opt += 1
            return result


    def mark_response(self, response):
        """
        Check if response matches the expected answer
        Parameter:
            response: str, response provided by candidate
        Returns:
            marks: int|float, marks awarded for the response.
        """
        
        if self.qtype == "short" or self.qtype == "single":
            if response == self.correct_answer:
                return self.marks 
            else:
                return 0.00

        elif self.qtype == "multiple":
            response = set(response.split(", "))
            correct_answer = set(self.correct_answer.split(", "))

            if response == correct_answer: 
                return self.marks
            elif response & correct_answer:
                correct_ans = len(response & correct_answer)
                mark = (correct_ans / len(correct_answer)) *  self.marks
                mark = round(mark, 2)
                return round(mark, 2)
            else:
                return 0.00

        else: 
            return None
            
            

    def preview_question(self, i=0, show=True):
        """
        Returns formatted string showing details of question.
        Parameters:
            i: int, placeholder for question number, DEFAULT = 0
            show: bool, True to show Expected Answers, DEFAULT = TRUE
        """
        
        marks = self.marks
        if i == 0: i = "X"
        else: i = i

        line1 = f"Question {i} - {self.qtype.capitalize()} Answer[{marks}]\n"
        line2 = f"{self.description}\n"
        line3 = f"Expected Answer: {self.correct_answer}"
        
        if self.qtype == "single" or self.qtype == "multiple":
            a = self.answer_options[0][0]
            b = self.answer_options[1][0]
            c = self.answer_options[2][0]
            d = self.answer_options[3][0]
            if self.qtype == "multiple": 
                line1 = f"Question {i} - {self.qtype.capitalize()} Answers[{marks}]\n"
            line_description = f"{a}\n{b}\n{c}\n{d}\n"
            sample_q = line1+line2+line_description+line3
                
        elif self.qtype == "short":
            line_description = f"{self.description}\n"
            sample_q = line1+line_description+line3

        elif self.qtype == "end":
            sample_q = "-End-"

        return sample_q

    def generate_order():
        """
        Returns a list of 4 integers between 0 and 3 inclusive to determine order.

        Sample usage:
        >>> generate_order()
            [3,1,0,2]
        """
        i = 0
        ls = [0, 1, 2, 3]
        new_ls = []
        while i < 4:  
            while True:
                num = random.randint(0,3)
                set_num = {num}
                set_ls = set(ls)
                if len(set_num & set_ls) == 1: break
            new_ls.append(num)
            ls.remove(num)
            i += 1
        return new_ls
        

    def shuffle_answers(self):
        """
        Updates answer options with shuffled elements.
        Must call generate_order only once.
        """

        if self.qtype == "single" or self.qtype == "multiple":
            shuffle = Question.generate_order()
            abcd = ["A","B","C","D"]
            answer = []
            correct_ans = ""
            original = self.answer_options
            
            i = 0
            while i < len(shuffle):
                order = shuffle[i]
                alphabet = abcd[i]
                description = f"{alphabet}.{original[order][0][2:]}"
                tup = (description, original[order][1])
                answer.append(tup)
                i+=1

                if self.answer_options[order][1]: #if we have correct answer (True)
                    if correct_ans: #check if we have have more than 1 correct answer (if it not an emty string)
                        correct_ans += f", {alphabet}"
                    else: 
                        correct_ans = alphabet

            self.answer_options = answer
            self.correct_answer = correct_ans
            return self.answer_options

        else:
            return self.answer_options
    
    def copy_question(self):
        original_question = Question(self.qtype)
        original_question.description = self.description
        original_question.answer_options = self.answer_options
        original_question.correct_answer = self.correct_answer
        original_question.marks = self.marks
        return original_question


    def __str__(self):
        '''
        You are free to change this, this is here for your convenience.
        When you print a question, it'll print this string.
        '''
        return f'''Question {self.__hash__()}:
Type: {self.qtype}
Description: {self.description}
Possible Answers: {self.get_answer_option_descriptions()}
Correct answer: {self.correct_answer}
Marks: {self.marks}
'''
