import json

answer = None

while answer not in ("c", "p"):
    print("c= Create a quiz?")
    print("p= Play a quiz?")
    answer = input("Please choose:\n")

    if answer == "c":
        print("ask_for_question")
        question = ask_for_question()
        answer_for_question = ask_for_answers()
        quiz_object = {"question": question, "ansers_for_question": answer_for_question}
        print(str(quiz_object))
        f = open('data.json', 'w')
        data.append(quiz_object)
        json.dump(data, f)
    elif answer == "p":
        print("Play")
    else:
        print("Please enter c or p.")

def ask_for_question():
    """ Ask user for question """
    while True:
        print("Please enter question\n")
        data_question = input("Question is:")

        question = data_question

        return question