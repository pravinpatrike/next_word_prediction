
# Next Word Prediction API

This project provides a simple FastAPI-based API for predicting the next word in a sequence using a pre-trained GPT-2 model.

---

## Project Structure

```
├── src
│   ├── utils.py
│   ├── model.py
│   ├── api.py
│   └── predict.py
├── venv
├── main.py
├── README.md
└── requirements.txt


```

* **`src/api.py`:** Defines the FastAPI app and the `/predict` endpoint.
* **`src/model.py`:**  Contains the function to load the pre-trained GPT-2 model and tokenizer.
* **`src/utils.py`:**  Provides utility functions for preprocessing text, encoding and decoding with the tokenizer, and generating the next word prediction.
* **`src/predict.py`:**  A script demonstrating how to interact with the API.
* **`venv`:** Contains the virtual environment for the project, which includes all the installed dependencies.
* **`main.py`:**  The main entry point for running the FastAPI application using uvicorn.
* **`README.md`:** Provides an overview and instructions for setting up and running the project.
* **`requirements.txt`:** Lists the dependencies required to run the project.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   ```

2. **Navigate to the project directory:**
   ```bash
   cd next-word-prediction-api
   ```

3. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the API

1. **Start the FastAPI server:**
   ```bash
   python main.py
   ```
   This will start the server at `http://127.0.0.1:8000`.

2. **Test the API:**
   - You can use the `src/predict.py` script to send requests to the API.
   - Alternatively, you can use tools like curl or Postman to send POST requests to the `/predict` endpoint with a JSON payload containing the `text` for prediction.

     Example using curl:
     ```bash
     curl -X POST -H "Content-Type: application/json" -d '{"text": "This is an example"}' http://127.0.0.1:8000/predict
     ```

## API Endpoint

**`/predict` (POST)**

* **Request Body:**
    ```json
    {
      "text": "This is a test" 
    }
    ```
* **Response Body:**
    ```json
    {
      "next_word": "sentence"
    }
    ```

## Notes

* The API uses a pre-trained GPT-2 model from Hugging Face Transformers.
* The `utils.py` file includes basic text preprocessing. You can add more sophisticated preprocessing steps as needed.
* The `predict.py` script demonstrates how to interact with the API using the `requests` library.

This README provides a basic overview of the project. You can expand it with more details about the model, potential use cases, limitations, etc.
```