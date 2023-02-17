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
    """ Ask user for quiz nane """
    while True:
        print("Please enter quiz name\n")
        data_name = input("Name for quiz:")

        quiz_name = data_name

        return quiz_name


def ask_for_question():
    """ Ask user for question """
    while True:
        print("Please enter question\n")
        data_question = input("Question is:")

        question = data_question

        return question


def ask_for_answers():
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

