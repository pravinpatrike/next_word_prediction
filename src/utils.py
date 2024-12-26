import torch
from transformers import GPT2Tokenizer

# Initialize the tokenizer once to avoid reloading in multiple places
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def preprocess_input(text: str) -> str:
    """
    Preprocess the input text before passing it to the model.
    """
    text = text.strip()  # Remove leading/trailing spaces
    # Add any other text cleaning steps here if necessary (e.g., remove punctuation)
    return text

def encode_input(text: str):
    """
    Tokenize the input text and return the encoded tensor.
    """
    inputs = tokenizer.encode(text, return_tensors="pt")
    return inputs

def decode_output(output_tensor) -> str:
    """
    Convert the model's output tensor into human-readable text.
    """
    decoded_text = tokenizer.decode(output_tensor[0], skip_special_tokens=True)
    return decoded_text

def generate_next_word(model, text: str) -> str:
    """
    Generate the next word using the pre-trained GPT-2 model (next token).
    """
    text = preprocess_input(text)  # Clean the input
    inputs = encode_input(text)    # Tokenize and encode the input
    
    # Get the model's output logits for the last token
    with torch.no_grad():
        outputs = model(inputs)
    
    # Get the logits for the last token and find the next token
    logits = outputs.logits
    next_token_logits = logits[0, -1, :]  # Get the logits for the last token
    next_token_id = torch.argmax(next_token_logits)  # Get the most likely next token
    
    # Decode the next token ID into a word
    next_word = tokenizer.decode(next_token_id)
    return next_word
