from googletrans import Translator
#first pip install googletrans==3.1.0a0
t = Translator()
#tests to see if api is working before running the translation method
t.translate('hola') # spanish for hello
t.translate('Привет') # russian for hello
t.translate('wat is jouw naam') # dutch for what is you name

def translation(userInput):
    Lang = t.translate(userInput)
    if Lang.detect(Lang) != t.translate(userInput, src='en'):  # if input is not english the api will translate it
        userInput = Lang.text
        return userInput
    elif Lang.detect(Lang) == t.translate(userInput, src='en'):  # if User types english it will return the english output
        return userInput


# to check if translator works use this to test the method
# --UPDATE --
# Every time a translation is passed it throws an error in which the
# translation does not work refer to documentation.
val = input("ask:")
print(translation(val))
