import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
question_wors = ["what", "why", "when", "where",
                 "name", "is", "how", "do", "does",
                 "which", "are", "could", "would",
                 "should", "has", "have", "whom", "whose", "don't"]

question = input("Input a sentence: ")
question = question.lower()
question = word_tokenize(question)

print(question)
