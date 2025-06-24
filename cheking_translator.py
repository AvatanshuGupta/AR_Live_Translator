from googletrans import Translator

translator = Translator()

text = "How are you? what is your name"

translated = translator.translate(text, src='en', dest='hi')
print("Original:", text)
print("Translated:", translated.text)
