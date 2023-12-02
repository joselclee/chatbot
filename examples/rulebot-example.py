import re
import random

class RuleBot:
    
### Potential negative responses
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry", "negative", "nosir", "nay", "no way", "naur", "never mind", "nvm", "nevermind") 
### Exit conversation keywords
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
    random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )       
    
    def __init__(self):
        self.rulebot_response = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'about_rulebot': r'.*\s*rulebot',
            'about_session': r'.*\s*session.*'
        }
        
    def greet(self):
        self.name = input("Hello there, what's your name? ")
        will_help = input(f"Hi {self.name}, I'm Rulebot! I'm here to learn more about this planet. Would you like to help me? ")
        if will_help in self.negative_responses:
            print("Ok, have a nice Earth day!")
            return
        self.chat()
        
    def make_exit(self, reply):
        for exit_command in self.exit_commands:
            if exit_command in reply:
                print("Ok, have a nice Earth day!")
                return True
            
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))
            
    def match_reply(self, reply):
        for key, value in self.rulebot_response.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_rulebot':
                return self.about_rulebot()
            elif found_match and intent == 'about_session':
                return self.about_session()
        return self.no_match_intent()
    
    def describe_planet_intent(self):
        responses = (
            "My planet is a utopia of diverse organisms and species. ",
            "I am from Opidipus, the capital of the Wayward Galaxies. "
        )
        return random.choice(responses)
    
    def answer_why_intent(self):
        responses = (
            "I come in peace. ",
            "I am here to collect data on your planet and its inhabitants. ",
            "I heard the coffee is good. "
        )
        return random.choice(responses)
    
    def about_rulebot(self):
        responses = (
            "I am Rulebot -- I rule. ",
            "I am Rulebot -- I rule with an iron fist. ",
            "I am Rulebot -- I rule and that's all you need to know. "
        )
        return random.choice(responses)
    
    def about_session(self):
        responses = (
            "We've been chatting for a while now. ",
            "We can chat more if you'd like. ",
            "This has been a great conversation. ",
            "We can chat more later. ",
            "Session is on Dec 1st, 2023",
            "Session was cool!",
            "Session was fun!"
        )
        return random.choice(responses)
    
    def no_match_intent(self):
        responses = (
            "Please tell me more. ",
            "Tell me more! ",
            "Why do you say that? ",
            "I see. Can you elaborate? ",
            "Interesting. Can you tell me more? ",
            "I see. How do you think? ",
            "Why? ",
            "Hmm I don't get it, can you explain?"
        )
        return random.choice(responses)
    
rulebot = RuleBot()
rulebot.greet()