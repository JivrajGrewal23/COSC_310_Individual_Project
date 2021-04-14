import wikipedia

def wordSplit(userInput):
    findPhrase = False
    i = userInput.lower()
    phrase = i.split()
    if phrase == "explain to me":
        findPhrase = True
    return findPhrase

def wikiLookup(userInput):
    phrase = userInput.lower().split()
    empty = ""

    for i in range(3, len(phrase)):
        empty = empty + phrase[i] + " "
    try:
        empty = wikipedia.summary(empty, sentences=1)
    except:
        empty = "Sorry, I could not find information on '" + empty + "'. Try a different topic."

    return empty

#this works if you run the file but when the chat bot runs it does not perform the wikipedia action i do not know why
val = input("ask")
print(wikiLookup(val))
