from transformers import Trainer, TrainingArguments
from andrev2 import prepare_dataset

def main():
    model, dataset, data_collator = prepare_dataset("train.csv")

    training_args = TrainingArguments(
        output_dir="./gpt2-fine-tuned",
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_total_limit=2,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=dataset,
    )

    trainer.train()

    model.save_pretrained("./gpt2-fine-tuned")

if __name__ == "__main__":
    main()
