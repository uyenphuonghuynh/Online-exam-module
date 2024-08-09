'''
Interface of the exam
'''
import setup
import program_two
import program_one
import sys
import candidate

def main(args):
    candidates = program_two.main(args)

    if not candidates:
        return

    attempt = 0

    
    while True:
        if attempt == 3:
            print("Contact exam administrator.")
            return

        user = input("Enter your student identification number (SID) to start exam: ")

        i = 0
        while i < len(candidates): 
            if not user.isdigit():
                print("Invalid SID.")
                attempt += 1
                break
            elif len(user) != 9:
                print("Invalid SID.")                    
                attempt += 1
                break

            if user == candidates[i].sid:
                print("Verifying candidate details...")
                attempt = 0
                while True:
                    name = input("Enter your full name as given during registration of exam: ")

                    if name.lower() == candidates[i].name.lower():
                        print("Start exam....\n")
                        #program_two.assign_exam(candidates[i].exam)
                        #candidates[i].do_exam(candidates[i].exam.shuffle)
                        #if candidates[i].exam.shuffle:
                        candidates[i].do_exam(False)
                        #else: 
                            #candidates[i].do_exam(True)
                        return


                    else:
                        if attempt == 2:
                            print("Contact exam administrator to verify documents.")
                            return

                        print("Name does not match records.")
                        attempt += 1

            
            if i == (len(candidates) - 1) and user != candidates[i].sid:
                print("Candidate number not found for exam.")
                attempt += 1
                while True:
                    again = input("Do you want to try again [Y|N]? ")
                    if again.lower() != "y" and again.lower() != "n":
                        print("Response must be [Y|N].")
                        continue
                    elif again.lower() == "n":
                        return 
                    elif again.lower() == "y":
                        break
            i += 1

    
if __name__ == "main":
    main(sys.argv) 
