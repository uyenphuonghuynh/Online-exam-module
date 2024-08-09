# Test Case Designs
Complete the given tables with details of your test case design for each question type.
State the values to initalize appropriate `Question` objects required for the test case.

Column descriptions:
* Test ID - Test case identification number
* Description - Type of testcase and brief explanation of test case details
* Inputs - Arguments into the method
* Expected Output - Return values of the method
* Status - pass/fail 

Table 1: Summary of test cases for method `mark_response` for question type `short`


| Test ID | Description |                                     Inputs                                                 |    Expected Output   |   Status   |
| ------- | ----------- | -------------------------------------------------------------------------------------------|----------------------|------------|
|   01    |  Positive   | def one(arg):                                                                              |                      |            |
|         |             |   assert Question.mark_response(arg, "Bob") == 1, "Correct answer isn't marked correctly"  | Test01 is successful |    Pass    |
|         |             |   print("Test01 is successful")                                                            |                      |            |
|         |             |                                                                                            |                      |            |
|   02    |  Negative   | def two(arg):                                                                              |                      |            |
|         |             |   assert Question.mark_response(arg, "BOB") == 0, "Incorrect answer is marked incorrectly" | Test02 is successful |    Pass    |
|         |             |   print("Test02 is successful")                


Table 2: Summary of test cases for method `mark_response` for question type `single`

| Test ID | Description |                                     Inputs                                                  | Expected Output     | Status |
| ------- | ----------- | --------------------------------------------------------------------------------------------| --------------------| ------ |
|    03   |  Positive   | def three(arg):                                                                             |                     |        |
|         |             |   assert Question.mark_response(arg, "D") == 1, "Correct answer is marked incorrectly"      |Test03 is successful |  Pass  |
|         |             |   print("Test 03 is successful")                                                            |                     |        |
|         |             |                                                                                             |                     |        |
|    04   |  Negative   | def four(arg):                                                                              |                     |        |
|         |             |   assert Question.mark_response(arg, "B") == 0, "Incorrect answer is marked incorrectly"    |Test04 is successful |  Pass  |
|         |             |   print("Test 04 is successful")                                                            |                     |        |

Table 3: Summary of test cases for method `mark_response` for question type `multiple`

| Test ID | Description | Inputs                                                                                          | Expected Output    | Status |
| ------- | ----------- | ------------------------------------------------------------------------------------------------|--------------------|--------|                                                                                      | --------------- | ------ |
|  05     | Positive    | def five(arg):                                                                                  |                    |        |
|         |             |    assert Question.mark_response(arg, "A, B, C") == 2, "Correct answer(s) is marked incorrectly"|Test05 is successful|  Pass  |
|         |             |    print("Test 05 is successful")                                                               |                    |        |
|         |             |                                                                                                 |                    |        |
|  06     |  Negative   | def six(arg):                                                                                   |                    |        |
|         |             |    assert Question.mark_response(arg, "A, D") == 1, "Incorrect answer(s) is marked incorrectly" |Test06 is successful|  Pass  |
|         |             |    print("Test 06 is successful")                                                               |                    |        |


