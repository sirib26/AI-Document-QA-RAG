from rag import ask_question

while True:
    q = input("Ask: ")
    print(ask_question(q))