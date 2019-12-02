import wikipedia , wolframalpha
while (True):
    UserQuery= input("Question :")
    try:
        app_id = "5X3QWJ-8WLKJA2PYG"
        client = wolframalpha.Client(app_id)
        result = client.query(UserQuery)
        answer = next(result.results).text
        print(answer)
    except:
        print(wikipedia.summary(UserQuery, sentences=5))