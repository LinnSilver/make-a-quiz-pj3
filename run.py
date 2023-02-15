
def run():
    # Opening JSON file
    f = open('data.json', 'r')

    # Load JSON data to memory
    try:
        data = json.load(f)
        if type(data) is not list:
            data = []
        f.close()
    except:
        print("Failed to read data from JSON")
        data = []

    import json
    answer = None

    while answer not in ("c", "p"):
        print("c= Create a quiz?")
        print("p= Play a quiz?")
        answer = input("Please choose:\n")

        if answer == "c":
            print("ask for quiz name")
            quiz_name = ask_for_name()

            print("ask_for_question")
            question = ask_for_question()
            answer_for_question = ask_for_answers()
            quiz_object = {"quiz_name":  quiz_name, 
                            "question": question, 
                            "answer_for_question": answer_for_question}
            print(str(quiz_object))
            f = open('data.json', 'w')
            data.append(quiz_object)
            json.dump(data , f)
            f.close()
        elif answer == "p":
            print("Play")
        else:
            print("Please enter c or p.")

def ask_for_name():
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
    number_of_answers = int(input("How many answers do you want to add?:"))

    i = 0
    answer_list = []
    while i < number_of_answers:
        print("Please enter answer\n")
        data_answer = input("Answer:")
        answer_list.append(data_answer)
        i += 1
    print("Wath is corect answer?")
    corect_answer = input()
    corect_answer_index = answer_list.index(corect_answer)
    if corect_answer_index >= 0:
        del answer_list[corect_answer_index]
        return {"answer":answer_list, "corect_answer": corect_answer}


if __name__ == '__main__':
    run()