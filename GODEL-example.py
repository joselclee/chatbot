# from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
# tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")
# model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")
# def generate(instruction, knowledge, dialog):
#     if knowledge != '':
#         knowledge = '[KNOWLEDGE] ' + knowledge
#     dialog = ' EOS '.join(dialog)
#     query = f"{instruction} [CONTEXT] {dialog} {knowledge}"
#     input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids
#     outputs = model.generate(input_ids, max_length=128, min_length=8, top_p=0.9, do_sample=True)
#     output = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return output
# # Instruction for a chitchat task
# instruction = f'Instruction: given a dialog context, you need to response empathically.'
# # Leave the knowldge empty
# knowledge = ''
# dialog = [
#     'Does money buy happiness?',
#     'It is a question. Money buys you a lot of things, but not enough to buy happiness.',
#     'What is the best way to buy happiness ?'
# ]
# response = generate(instruction, knowledge, dialog)
# print(response)

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")
model = AutoModelForSeq2SeqLM.from_pretrained("microsoft/GODEL-v1_1-large-seq2seq")

def generate(instruction, knowledge, user_input):
    if knowledge != '':
        knowledge = '[KNOWLEDGE] ' + knowledge
    dialog = user_input
    query = f"{instruction} [CONTEXT] {dialog} {knowledge}"
    input_ids = tokenizer(f"{query}", return_tensors="pt").input_ids
    outputs = model.generate(input_ids, max_length=128, min_length=8, top_p=0.9, do_sample=True)
    output = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return output

# Instruction for a chitchat task
instruction = f'Instruction: given a dialog context, you need to response empathically.'
# Leave the knowledge empty
knowledge = ''

# Get user input for the dialog
user_input = input("User: ")

# Call the generate function with user input
response = generate(instruction, knowledge, user_input)
print("Bot:", response)
