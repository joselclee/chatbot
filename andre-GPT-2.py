from transformers import GPT2LMHeadModel, GPT2Tokenizer

def chat_with_gpt2():
    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    conversation_history = []

    print("Bot: Hello! I'm your chatbot. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Bot: Goodbye! Have a great day.")
            break

        # Add user input to the conversation history
        conversation_history.append("You: " + user_input)

        # Tokenize and generate a response
        input_ids = tokenizer.encode('\n'.join(conversation_history), return_tensors='pt')
        output = model.generate(input_ids, attention_mask=input_ids, do_sample=True, max_length=100, num_beams=5, no_repeat_ngram_size=2, pad_token_id=tokenizer.eos_token_id)

        # Decode and display the bot's response
        bot_response = tokenizer.decode(output[0], skip_special_tokens=True)
        print("Bot:", bot_response)

        # Add bot's response to the conversation history
        conversation_history.append("Bot: " + bot_response)

if __name__ == "__main__":
    chat_with_gpt2()



