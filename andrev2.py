<<<<<<< Updated upstream
import pandas as pd
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling
=======
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, PreTrainedTokenizer

import torch
>>>>>>> Stashed changes

def prepare_dataset(dataset_path):
    model_name = "gpt2-large"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    df = pd.read_csv(dataset_path)
    df["input_text"] = df["instruction"] + " " + df["responses"] + " " + df["next_response"]

    tokenized_data = tokenizer(
        df["input_text"].tolist(),
        text_pair=df["answer"].tolist(),
        padding=True,
        truncation=True,
        max_length=128,
    )

<<<<<<< Updated upstream
    dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=None,
        block_size=128,
        overwrite_cache=True,
        **tokenized_data
    )
=======
        # Generate a response while limiting the total chat history to 1000 tokens
        chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.bos_token_id)
>>>>>>> Stashed changes

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )

    return model, dataset, data_collator
