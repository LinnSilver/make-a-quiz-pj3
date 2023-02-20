import json


def storage_get():
    """ Manage JSON file """

    global data

    with open('data.json') as json_file:
        try:
            data = json.load(json_file)
        except ValueError:
            data = {}


def storage_save():
    """ Save to json file """
    # Serializing json
    json_object = json.dumps(data)

    # Writing to data.json
    with open("data.json", "w") as outfile:
        outfile.write(json_object)


def run_menu():
    """  """
    answer = None

    while answer not in ("c", "p"):
        print("\nc= Create a quiz?")
        print("p= Play a quiz?")
        answer = input("\nPlease choose c or p: \n")

        if answer == "c":
            create_quiz()
        elif answer == "p":
            print("Play a quiz")
        else:
            print("Please enter c or p.")


def create_quiz():
    """ Ask user for quiz name """
    global data

    quiz_questions = data

    quiz_name = input("\nPlease enter quiz name: ")

    quiz_name = quiz_name.strip()

    if len(quiz_name) < 2:
        print("Please enter a name that is at least 2 characters long.")
        create_quiz()

    print(quiz_name)

    question_status = True
    while question_status == True:

        quiz_question_name = create_quiz_question()
        answers = create_quiz_question_answers()

        correct_answer = create_quiz_question_answers_set_correct_answer(answers)

        quiz_questions[quiz_name] = {quiz_question_name: {
                                            "question": quiz_question_name, 
                                            "answers": answers,
                                            "correct_answer": correct_answer}}
        if create_quiz_question_next() == False:

            data = quiz_questions
            storage_save()
            return True


def create_quiz_question_next():
    """ Ccreate_quiz_question_next """
    quiz_question = input("\nAdd one more question? (Y/N default No): ")

    if (quiz_question == "Y") or (quiz_question == "y"):
        return True
    else:
        return False


def create_quiz_question():
    """ Create_quiz_question """
    quiz_question = input("\nPlease enter quiz question: ")

    quiz_question = quiz_question.strip()

    if len(quiz_question) < 3:
        print("Please enter a question that is at least 3 characters long.")
        create_quiz_question()
        return 

    print(quiz_question)

    return quiz_question


def create_quiz_question_answers_next():
    """ create quiz question answers next """
    question_answers = input("\nAdd one more answer? (Y/N default No): ")

    if (question_answers == "Y") or (question_answers == "y"):
        return True
    else:
        return False


def create_quiz_question_answers():
    """ Ask user for answers """
    answers_list = []
    answer_status = True
    while answer_status == True:
        question_answers = input("\nPlease enter answer: ")
        question_answers = question_answers.strip()

        if len(question_answers) < 1:
            print("Please enter a answer that is at least 1 characters long.")
        else:
            answers_list.append(question_answers)
            answer_status = create_quiz_question_answers_next()

    return answers_list


def create_quiz_question_answers_set_correct_answer(answer_list):
    """ create_quiz_question"""

    for value in answer_list:
        print('Option: ' + value) 

    corect_answer = input("\nAt last, enter corect answer: ")
    corect_answer = corect_answer.strip()

    for value in answer_list:
        if (value == corect_answer):
            return corect_answer

    create_quiz_question_answers_set_correct_answer(answer_list)


if __name__ == '__main__':
    storage_get()
    run_menu()
