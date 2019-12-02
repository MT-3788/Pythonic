import wikipedia
while(True):
    UserQuery = input("Question: ")
    #wikipedia.set_lang("eng")
        print(wikipedia.summary(UserQuery,sentences=7))
