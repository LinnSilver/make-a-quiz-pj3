import json
global data


def storage_get():
    """ Manage JSON file """
    # Opening JSON file
    storage_json = open('data.json', 'r')

    # Load JSON data to memory
    try:
        data = json.load(storage_json)
        if type(data) is not list:
            data = []
        storage_json.close()
    except:
        print("Failed to read data from JSON")
        data = []


def run_menu():
    answer = None

    while answer not in ("c", "p"):
        print("c= Create a quiz?")
        print("p= Play a quiz?")
        answer = input("Please choose c or p:\n")

        if answer == "c":
            create_quiz()
        elif answer == "p":
            print("Play a quiz")
        else:
            print("Please enter c or p.")


def create_quiz():
    """ Ask user for quiz name """

    quiz_questions = []

    quiz_name = input("Please enter quiz name: ")

    quiz_name.strip()

    if len(quiz_name) < 2:
        print("Please enter a name that is at least 2 characters long.\n")
        create_quiz()

    print(quiz_name)

    question_status = True
    while question_status == True:

        quiz_question_name = create_quiz_question()
        answers = create_quiz_question_answers()


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


def create_quiz_question_answers():
    """ Ask user for answers """
    number_of_answers = int(input("How many answers do you want to add?:"))
    answer_list = []
    #i = 0
    
    for i in range(number_of_answers):
        data_answer = input("Please enter answer:\n")
        answer_list.append(data_answer)

    while True:
        corect_answer = input("Wath is corect answer:?\n")
   
        if corect_answer not in answer_list:
            print("Please enter one of the ansers you provided.")
       
        return {"answer": answer_list, "corect_answer": corect_answer}


if __name__ == '__main__':
    storage_get()
    run_menu()

