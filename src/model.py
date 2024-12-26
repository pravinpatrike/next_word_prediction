from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_model():
    """
    Loads the pre-trained GPT-2 model and tokenizer.
    """
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    return model, tokenizer
