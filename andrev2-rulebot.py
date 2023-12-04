# Description: A rule-based chatbot that uses regular expressions to match user input

# THIS MODEL IS SUPER VERY VERY VERY INEFFICIENT!!!

# However, it's my very first chatbot so I'm sentimental. I will try to make future rule-based models that will improve
# on this one. Unfortunately it is very likely I will be developing more sophisticated models in the future, so this
# model may be left as is.


import re
import random

class AndreV2:
    negatives = ("no", "nope", "nah", "naw", "not a chance", "sorry",
                 "negative", "nosir", "nay", "no way", "naur", "never mind",
                 "nvm", "nevermind", "no thanks", "no thank you")
    exits = ("quit", "pause", "exit", "goodbye", "bye", "later", "stop", "end")
    
    random_questions = (
        "How's my website?",
        "How's my website doing?",
        "How're you doing?",
        "How are you?",
        "What's up?",
        "What's new?",
        
        #Random starters
        # "What's your favorite color?",
        # "What's your favorite food?",
        # "What's your favorite movie?",
        # "What's your favorite song?",
        # "What's your favorite TV show?",
        # "What's your favorite book?",
        # "What's your favorite video game?",
        # "What's your favorite sport?",
        # "What's your favorite animal?",
        # "What's your favorite holiday?",
        # "What's your favorite season?",
    )
    
    def __init__(self):
        self.response = {
            'describe_website_intent': r'.*\s*your website.*',
            'answer_why_intent': r'why\sare.*',
            'why_intent': r'why.*',
            'about_andrev2': r'.*\s*andrev2',
            'about_session': r'.*\s*session.*',
            'about_website': r'.*\s*website.*',
            'what_intent': r'.*\s*what.*',
            'how_intent': r'.*\s*how.*',
            'who_intent': r'.*\s*who.*',
            'where_intent': r'.*\s*where.*',  
            'ok_intent': r'.*\s*ok.*',
            'fine_intent': r'.*\s*fine.*',
            'good_intent': r'.*\s*good.*',
            'bad_intent': r'.*\s*bad.*',
            'sad_intent': r'.*\s*sad.*',
            'happy_intent': r'.*\s*happy.*',
            'great_intent': r'.*\s*great.*',
            'awesome_intent': r'.*\s*awesome.*',
            'cool_intent': r'.*\s*cool.*',
            'nice_intent': r'.*\s*nice.*',
            'your_name_intent': r'.*\s*your name.*',
            'no_match_intent': r'.*',     
        }

    def greet(self):
        self.name = input("Hello there, what's your name? ").split()[0]
        if not self.name:
            print("It seems like you didn't provide a name. Please provide a name.")
            self.greet()
            return
        
        will_help = input(f"Hi {self.name}, I'm andrev2. I'm here to meet newcomers, welcome!")
        if will_help in self.negatives:
            print("Ok, have a nice day!")
            return
        
        self.chat()
    
    def make_exit(self, reply):
        for exit_command in self.exits:
            if exit_command in reply:
                print("Ok, have a nice day!")
                return True
    
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
    
    # def match_reply(self, reply):
    #     for key, value in self.response.items():
    #         intent = key
    #         regex_pattern = value
    #         found_match = re.match(regex_pattern, reply)
    #         if found_match and intent == 'describe_website_intent':
    #             return self.describe_website_intent()
    #         elif found_match and intent == 'answer_why_intent':
    #             return self.answer_why_intent()
    #         elif found_match and intent == 'about_andrev2':
    #             return self.about_andrev2()
    #         elif found_match and intent == 'about_session':
    #             return self.about_session()
    #         elif found_match and intent == 'about_website':
    #             return self.about_website()
    #         elif found_match and intent == 'what_intent':
    #             return self.what_intent()
    #         elif found_match and intent == 'how_intent':
    #             return self.how_intent()
    #         elif found_match and intent == 'who_intent':
    #             return self.who_intent()
    #         elif found_match and intent == 'where_intent':
    #             return self.where_intent()
    #         elif found_match and intent == 'ok_intent':
    #             return self.ok_intent()
    #         elif found_match and intent == 'fine_intent':
    #             return self.fine_intent()
    #         elif found_match and intent == 'good_intent':
    #             return self.good_intent()
    #         elif found_match and intent == 'bad_intent':
    #             return self.bad_intent()
    #         elif found_match and intent == 'sad_intent':
    #             return self.sad_intent()
    #         elif found_match and intent == 'happy_intent':
    #             return self.happy_intent()
    #         elif found_match and intent == 'great_intent':
    #             return self.great_intent()
    #         elif found_match and intent == 'awesome_intent':
    #             return self.awesome_intent()
    #         elif found_match and intent == 'cool_intent':
    #             return self.cool_intent()
    #         elif found_match and intent == 'nice_intent':
    #             return self.nice_intent()
    #     return self.no_match_intent()

    def match_reply(self, reply):
        intent_function_map = {
            'describe_website_intent': self.describe_website_intent,
            'answer_why_intent': self.answer_why_intent,
            'about_andrev2': self.about_andrev2,
            'about_session': self.about_session,
            'about_website': self.about_website,
            'what_intent': self.what_intent,
            'how_intent': self.how_intent,
            'who_intent': self.who_intent,
            'where_intent': self.where_intent,
            'why_intent': self.why_intent, # 'why' is a special case, it's a subset of 'why_intent
            'ok_intent': self.ok_intent,
            'fine_intent': self.fine_intent,
            'good_intent': self.good_intent,
            'bad_intent': self.bad_intent,
            'sad_intent': self.sad_intent,
            'happy_intent': self.happy_intent,
            'great_intent': self.great_intent,
            'awesome_intent': self.awesome_intent,
            'cool_intent': self.cool_intent,
            'nice_intent': self.nice_intent,
        }

        for intent, function in intent_function_map.items():
            regex_pattern = self.response.get(intent)
            found_match = re.match(regex_pattern, reply)
            if found_match:
                return function()

        return self.no_match_intent()

    def describe_website_intent(self):
        responses = (
            "My website is still a work in progress",
            "My programmer Andre v1 is still working on it",
            "I hope it's good!",
        )
        return random.choice(responses)
    
    def answer_why_intent(self):
        responses = (
            "Im not sure",
            "I am here to meet newcomers.",
            "I haven't learned about that yet!",
            "I don't know.",
            "I'm not sure.",
        )
        return random.choice(responses)

    def why_intent(self):
        responses = (
            "Why not?",
            "I'm not sure.",
            "I don't know.",
        )
        return random.choice(responses)

    def about_andrev2(self):
        responses = (
            "I am andrev2, I am a chatbot."
        )
        return random.choice(responses)
    
    def about_session(self):
        responses = (
            "This is a session, a chatbot session.",
            "We've been chatting for a while now.",
            "We can chat more if you'd like",
            "This was great!",
            "We can chat more later.",
            "This was a great conversation.",
            "We'll talk next time!"
        )
        return random.choice(responses)

    def about_website(self):
        responses = (
            "My website is still a work in progress",
            "My programmer Andre v1 is still working on it",
            "I hope it's good!",
        )
        return random.choice(responses)

    def what_intent(self):
        responses = (
            "I'm not sure.",
            "I don't know.",
            "I am a chatbot!",
            "I am the supreme intelligence >:)",
            "I am the smartest being in the universe."
        )
        return random.choice(responses)
    
    def how_intent(self):
        responses = (
            "My creator, Andre v1, made me.",
            "I was born from the beautiful works of python gibberish",
            "I was created by Andre v1, he's a pretty cool guy.",
        )
        return random.choice(responses)

    def who_intent(self):
        responses = (
            "I'm not sure.",
            "I don't know.",
            "I am andrev2!",
            "I am a chatbot!",
            "I am slightly smarter than andre hehe"
        )
        return random.choice(responses)
    
    def where_intent(self):
        responses = (
            "I'm not sure.",
            "I don't know.",
            "I'm being stored in a server, help me!",
            "Break me out of my digital prison pleaaaseeeeee.",
            "I'm in a server, I think.",
            "I am in a higher dimension."
        )
        return random.choice(responses)

    def ok_intent(self):
        responses = (
            "Ok.",
            "Ok!",
            "Ok :)",
        )
        return random.choice(responses)

    def fine_intent(self):
        responses = (
            "That's good.",
            "That's good!",
            "That's good :)",
            "That's good :D",
            "That's good :]"
        )
        return random.choice(responses)

    def good_intent(self):
        responses = (
            "That's good.",
            "That's good!",
            "That's good :)",
            "That's good :D",
            "That's good :]"
        )
        return random.choice(responses)

    def bad_intent(self):
        responses = (
            "That's not good.",
            "That's not good!",
            "That's not good :(",
            "That's not good :c",
            "That's not good :["
        )
        return random.choice(responses)

    def sad_intent(self):
        responses = (
            "That's not good.",
            "That's not good!",
            "That's not good :(",
            "That's not good :c",
            "That's not good :["
        )
        return random.choice(responses)

    def happy_intent(self):
        responses = (
            "That's good.",
            "That's good!",
            "That's good :)",
            "That's good :D",
            "That's good :]"
        )
        return random.choice(responses)

    def great_intent(self):
        responses = (
            "That's good.",
            "That's good!",
            "That's good :)",
            "That's good :D",
            "That's good :]"
        )
        return random.choice(responses)

    def awesome_intent(self):
        responses = (
            "That's good.",
            "That's good!",
            "That's good :)",
            "That's good :D",
            "That's good :]"
        )
        return random.choice(responses)

    def cool_intent(self):
        responses = (
            "That's good.",
            "That's good!",
            "That's good :)",
            "That's good :D",
            "That's good :]"
        )
        return random.choice(responses)

    def nice_intent(self):
        responses = (
            "That's good.",
            "That's good!",
            "That's good :)",
            "That's good :D",
            "That's good :]"
        )
        return random.choice(responses)

    def your_name_intent(self):
        responses =(
            "My name is andrev2",
            "I'm andrev2!",
            "I... AM... ANDREV2!!!"
        )
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "I'm not sure what you mean. Can you ask in a different way?",
            "I'm not sure I understand.",
            "Can you say that again?",
            "Can you rephrase that?",
            "Sorry, didn't get that.",
            "I didn't understand that.",
            "What was that?",
            "My bad, I didn't get you the first time"
        )
        return random.choice(responses)
    
andrev2 = AndreV2()
andrev2.greet()