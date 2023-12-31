import numpy as np
import nltk
import random
import string # to process standard python strings

file = open('input.txt','r',errors = 'ignore')
raw_doc = file.read()
raw_doc = raw_doc.lower(); # converts to lowercase
nltk.download('punkt') # Using Punkt tokenizer
nltk.download('wordnet') # Using the wordnet dictionary
nltk.download('omw-1.4') 

sentence_tokens = nltk.sent_tokenize(raw_doc)# converts to list of sentences
word_tokens = nltk.word_tokenize(raw_doc)# converts to list of words

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

greet_inputs = ("hello", "hi", "greetings", "sup", "what's up","hey", "yo", "hiya", "howdy")
greet_responses = ["hi", "hey", "*nods*", "hi there", "hello", "how are you", "yo", "aye" ]

def greet(sentence):
    for word in sentence.split():
        if word.lower() in greet_inputs:
            return random.choice(greet_responses)
        
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def response(user_response):
    bot_response=''
    sentence_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, token_pattern=None)
    tfidf = TfidfVec.fit_transform(sentence_tokens)
    
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        bot_response=bot_response+"I haven't the slightest what that is."
        return bot_response
    else:
        bot_response = bot_response+sentence_tokens[idx]
        return bot_response
    
flag = True
print("Hello! My name is Billiam and I am at your service. Please type Bye if you no longer wish to speak to me.")

while flag:
    user_response = input()
    user_response = user_response.lower()
    
    if user_response not in ['bye', 'bye!', 'goodbye', 'goodbye!']:
        if user_response == 'thanks' or user_response == 'thank you':
            flag = False
            print("You are welcome..")
        else:
            if greet(user_response) is not None:
                print("Billiam: " + greet(user_response))
            else:
                print("Billiam: ", end="")
                print(response(user_response))
                sentence_tokens.remove(user_response)
    else:
        flag = False
        print("Billiam: Farewell thee...")
