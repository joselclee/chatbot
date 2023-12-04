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

greet_inputs = ("hello", "hi", "greetings", "sup", "what's up","hey",)
greet_responses = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greet(sentence):
    for word in sentence.split():
        if word.lower() in greet_inputs:
            return random.choice(greet_responses)
        
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def response(user_response):
    bot_response=''
    sentence_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize)
    tfidf = TfidfVec.fit_transform(sentence_tokens)
    
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        bot_response=bot_response+"I'm sorry, I don't understand!"
        return bot_response
    else:
        bot_response = bot_response+sentence_tokens[idx]
        return bot_response
    
flag = True
print("Hey, I'm NLTK-Bot. I will answer your queries about topics regarding nuclear science. If you want to exit, type Bye!")

while(flag==True):
    user_response = input()
    user_response=user_response.lower()
    
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            flag=False
            print("You are welcome..")
        else:
            if(greet(user_response)!=None):
                print("NLTKBot: "+greet(user_response))
            else:
                print("NLTKBot: ",end="")
                print(response(user_response))
                sentence_tokens.remove(user_response)
    else:
        flag=False
        print("Bot: Bye! take care..")