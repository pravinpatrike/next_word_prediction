from fastapi import FastAPI
from pydantic import BaseModel
from src.model import load_model
from src.utils import generate_next_word

app = FastAPI()

# Load pre-trained model once when the app starts
model, tokenizer = load_model()

# Define the input model for POST request
class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict(input_data: TextInput):
    """
    Endpoint to predict the next word based on the input.
    """
    next_word = generate_next_word(model, input_data.text)
    return {"next_word": next_word}
