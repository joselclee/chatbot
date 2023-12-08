import pandas as pd
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling

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

    dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=None,
        block_size=128,
        overwrite_cache=True,
        **tokenized_data
    )

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )

    return model, dataset, data_collator
