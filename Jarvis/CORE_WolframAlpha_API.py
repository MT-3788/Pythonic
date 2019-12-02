import wolframalpha
UserQuery = input("Question: ")
app_id = "5X3QWJ-8WLKJA2PYG"
client = wolframalpha.Client(app_id)
result = client.query(UserQuery)
answer = next(result.results).text
print(answer)
