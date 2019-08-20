import nltk
import numpy as np
import random
import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

f = open('info.txt', 'r')
raw = f.read()

sentence_tokens = nltk.sent_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "whats up", "hey")
GREETING_RESPONSES = ("hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me")


def greeting(sentence):
    sentence = re.sub(r'[^\w\s]', '', sentence)
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


def response(userInput):
    sentence_tokens.append(userInput)
    TfidVec = TfidfVectorizer(tokenizer=LemNormalize)
    tfidf = TfidVec.fit_transform(sentence_tokens)

    vals = cosine_similarity(tfidf[-1], tfidf)

    flat = vals.flatten()

    idx = flat.argsort()[-2]

    flat.sort()

    best_response = flat[-2]

    if best_response == 0:
        return "I don't know that"
    else:
        return sentence_tokens[idx]


print("ROBOTBOT: My name is RobotBot. I will answer queries about Robots. If you want to exit type bye")
name = input("Whats your name? ")
while True:
    userInput = input(name + ": ").lower()
    print("ROBOTBOT: ", end="")
    if userInput != 'bye':
        if greeting(userInput) is not None:
            print(greeting(userInput))
        else:
            print(response(userInput))
            sentence_tokens.remove(userInput)
    else:
        print("Bye!")
        break
