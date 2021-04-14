import wikipedia


# first pip install wikipedia
def wordSplit(userInput):
    findPhrase = False
    phrase = userInput.lower().split()
    if phrase == "explain to me":  # finds key phrase asked and then sends to another method
        findPhrase = True
    return findPhrase


def wikiLookup(userInput):
    phrase = userInput.lower().split()
    empty = ""
    phraseLen = len(phrase)  # checks to see if the length of user input is 3
    for i in range(3, phraseLen):
        empty = empty + phrase[i] + " "  # sees if user entered explain to me
    try:
        empty = wikipedia.summary(empty,
                                  sentences=1)  # checks wikipedia for the users input in conjuction with the key phrase.
    except:
        empty = "Sorry, '" + empty + "' is not specific enough for a search. Please enter the name agian but be more " \
                                     "specific. "

    return empty


# this works if you run the file but when the chat bot runs it does not perform the wikipedia action i do not know why
val = input("ask")
print(wikiLookup(val))
