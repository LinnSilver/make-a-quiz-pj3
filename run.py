import json


def storage_get():
    """
    Get data from JSON file
    """
    global data

    with open('data.json') as json_file:
        try:
            data = json.load(json_file)
        except ValueError:
            data = {}


def run_menu():
    """
    Asks the user to choose whether to create or play a quiz
    Validates input. Repeats until correct answer
    """
    answer = None

    while answer not in ("c", "p"):
        print("\nWelcome to your best quiz!")
        print("\nDo you Want to create or play a quiz??")
        print("\nC = Create a quiz?")
        print("P = Play a quiz?")
        answer = input("\nPlease choose c or p: ").lower().strip()

        if answer == "c":
            create_quiz()
        elif answer == "p":
            choose_quize_to_play()
        else:
            print("Please enter c or p.")


def choose_quize_to_play():
    """
    Prints quiz names to choose from.
    Asks user to choose which quiz to play.
    Validates input. Repeats until correct answer
    """
    dict = (data)
    keys_list = [key for key in dict]

    print("\nChoose which quiz to play."
          "\nYou can copy and paste questions and answers with the mouse.\n")

    for key, value in dict.items():
        print(key)

    quiz_name = None
    while quiz_name not in (keys_list):

        quiz_name = input("\nPlease choose quiz to play: ").strip()

        for key, value in dict.items():
            if quiz_name == key:
                play_quiz(quiz_name, value)
                return quiz_name


def play_quiz(quiz_name, quiz_data):
    """
    Print's question
    Print answers to choose from
    Validates input. Compare answers with the correct answer
    Keeps score
    When the quiz is over, prints the user score
    """
    score = 0

    for question, question_data in quiz_data.items():
        print('\nQuestion: ', question)

        print("\nWhich answer is correct?\n")

        for answers in question_data['answers']:
            print(answers)

        quiz_guess = input("\nWrite your answer: ").strip()

        if quiz_guess == question_data['correct_answer']:
            score = score + 1
            print("You were right!")

    print("\nYour score is: ", score)
    print("\nThank you for playing!")


def storage_save():
    """
    Serializing json and Writing to data.json
    """
    global data

    json_object = json.dumps(data, sort_keys=True, indent=4)

    with open("data.json", "w") as outfile:
        outfile.write(json_object)


def create_quiz():
    """
    Ask user for quiz name
    Validates input. Repeats until correct answer
    Collects quiz components
    Returns quiz data
    """
    global data

    quiz_name = input("\nPlease enter quiz name: ")

    quiz_name = quiz_name.strip()

    if len(quiz_name) < 2:
        print("Please enter a name that is at least 2 characters long.")
        create_quiz()

    print(quiz_name)

    question_data = {}
    question_status = True

    while question_status:

        quiz_question = create_quiz_question()
        answers = create_quiz_question_answers()
        correct_answer = create_quiz_question_answers_correct_answer(answers)

        question_data[quiz_question] = {
                                    "answers": answers,
                                    "correct_answer": correct_answer
                                    }
        if not create_quiz_question_next():

            data[quiz_name] = question_data

            storage_save()
            return True


def create_quiz_question_next():
    """
    Asking the user if they want to create another question
    Validates input
    """
    quiz_question = input("\nAdd one more question? (Y/N default Yes): ")

    if (quiz_question == "N") or (quiz_question == "n"):
        return False
    else:
        return True


def create_quiz_question():
    """
    Asking the user for quiz question
    Validates input. Repeats until correct question
    """
    quiz_question = input("\nPlease enter quiz question: ")

    quiz_question = quiz_question.strip()

    if len(quiz_question) < 3:
        print("Please enter a question that is at least 3 characters long.")
        create_quiz_question()
        return

    print(quiz_question)

    return quiz_question


def create_quiz_question_answers_next():
    """
    Asks the user if they want to create another answer
    Validates input
    """
    question_answers = input("\nAdd one more answer? (Y/N default Yes): ")

    if (question_answers == "N") or (question_answers == "n"):
        return False
    else:
        return True


def create_quiz_question_answers():
    """
    Asks the user to enter an answer to the question
    Validates input
    Returns list of answers
    """
    answers_list = []
    answer_status = True
    while answer_status:
        question_answers = input("\nPlease enter answer: ")
        question_answers = question_answers.strip()

        if len(question_answers) < 1:
            print("Please enter an answer that is at least 1 character long.")
        else:
            answers_list.append(question_answers)
            answer_status = create_quiz_question_answers_next()

    return answers_list


def create_quiz_question_answers_correct_answer(answer_list):
    """
    Asks the user to enter correct answer
    Validates that the correct answer is included in the list of answers
    Repeated until the correct answer matches an answer in answers
    """
    for value in answer_list:
        print('Your answers: ' + value)

    correct_answer = input("\nAt last, enter correct answer: "
                           "\nYou can copy and paste the correct answer"
                           " with the mouse.\n")
    correct_answer = correct_answer.strip()

    for value in answer_list:
        if value == correct_answer:
            return correct_answer

    return create_quiz_question_answers_correct_answer(answer_list)


if __name__ == '__main__':
    storage_get()
    run_menu()
