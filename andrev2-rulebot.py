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
            'what_intent': r'what.*',
            'how_intent': r'how.*',
            'who_intent': r'who.*',
            'where_intent': r'where.*'     
            'ok_intent': r'ok.*',
            'fine_intent': r'fine.*',
            'good_intent': r'good.*',
            'bad_intent': r'bad.*',
            'sad_intent': r'sad.*',
            'happy_intent': r'happy.*',
            'great_intent': r'great.*',
            'awesome_intent': r'awesome.*',
            'cool_intent': r'cool.*',
            'nice_intent': r'nice.*',
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
    
    def match_reply(self, reply):
        for key, value in self.response.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_website_intent':
                return self.describe_website_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_andrev2':
                return self.about_andrev2()
            elif found_match and intent == 'about_session':
                return self.about_session()
            elif found_match and intent == 'about_website':
                return self.about_website()
            elif found_match and intent == 'what_intent':
                return self.what_intent()
            elif found_match and intent == 'how_intent':
                return self.how_intent()
            elif found_match and intent == 'who_intent':
                return self.who_intent()
            elif found_match and intent == 'where_intent':
                return self.where_intent()
            elif found_match and intent == 'ok_intent':
                return self.ok_intent()
            elif found_match and intent == 'fine_intent':
                return self.fine_intent()
            elif found_match and intent == 'good_intent':
                return self.good_intent()
            elif found_match and intent == 'bad_intent':
                return self.bad_intent()
            elif found_match and intent == 'sad_intent':
                return self.sad_intent()
            elif found_match and intent == 'happy_intent':
                return self.happy_intent()
            elif found_match and intent == 'great_intent':
                return self.great_intent()
            elif found_match and intent == 'awesome_intent':
                return self.awesome_intent()
            elif found_match and intent == 'cool_intent':
                return self.cool_intent()
            elif found_match and intent == 'nice_intent':
                return self.nice_intent()
        return self.no_match_intent()

    def describe_website_intent(self):
        responses = (
            "My website is still a work in progress",
            "My programmer Andre v1 is still working on it",
            "I hope it's good!",
        )
        return random.choice(responses)
    def why_intent(self):
        responses = (
            "Why not?",
            "I'm not sure.",
            "I don't know.",
        )
        return random.choice(responses)

    def who_intent(self):
        responses = (
            "I'm not sure.",
            "I don't know.",
        )
        return random.choice(responses)
    
    def where_intent(self):
        responses = (
            "I'm not sure.",
            "I don't know.",
        )
        return random.choice(responses)
    
    def what_intent(self):
        responses = (
            "I'm not sure.",
            "I don't know.",
        )
        return random.choice(responses)
    
    def answer_why_intent(self):
        responses = (
            "Im not sure",
            "I am here to meet newcomers.",
            "I haven't learned about that yet!",
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
    
    def 
    
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