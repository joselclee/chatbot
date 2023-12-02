import torch
from transformers import BertTokenizer, BertForQuestionAnswering
from transformers import BertTokenizer, BertForQuestionAnswering
import torch
import random
import rasa

# Load BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForQuestionAnswering.from_pretrained("bert-base-uncased")

# Load Rasa NLU model
interpreter = rasa.nlu.model.Interpreter.load("path/to/your/nlu/model")

# Intent recognition function
def recognize_intent(user_input):
    result = interpreter.parse(user_input)
    intent = result["intent"]["name"]
    return intent

# BERT-based response generation function
def generate_response_bert(question, context):
    inputs = tokenizer(question, context, return_tensors="pt")
    outputs = model(**inputs)
    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits) + 1
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end]))
    return answer

# Dialogue management function
def manage_dialogue(intent, user_input, context):
    if intent == "greet":
        return "Hi there! How can I assist you today?"
    elif intent == "goodbye":
        return "Goodbye! Have a great day."
    elif intent == "ask_question":
        return generate_response_bert(user_input, context)
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# User feedback loop
def get_user_feedback(response):
    user_feedback = input(f"Was the response '{response}' helpful? (yes/no): ")
    # You can handle feedback here, e.g., update a feedback database
    if user_feedback.lower() == "no":
        print("I'm sorry to hear that. Please provide more details for improvement.")

# Main chatbot loop
context = ""
print("Chatbot: Hi, I'm your assistant. How can I help you today? Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    
    intent = recognize_intent(user_input)
    response = manage_dialogue(intent, user_input, context)
    
    print(f"Chatbot: {response}")
    get_user_feedback(response)
