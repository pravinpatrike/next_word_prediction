import requests

# Define the FastAPI server URL
API_URL = "http://127.0.0.1:8000/predict"

def get_prediction(text: str):
    """
    Send a POST request to the FastAPI /predict endpoint to get the next word prediction.
    """
    response = requests.post(API_URL, json={"text": text})
    
    if response.status_code == 200:
        prediction = response.json().get("next_word")
        return prediction
    else:
        return f"Error: {response.status_code}"

def main():
    input_text = input("Enter text for prediction: ")  # User input
    prediction = get_prediction(input_text)  # Get prediction by calling FastAPI endpoint
    print(f"Predicted next word: {prediction}")

if __name__ == "__main__":
    main()
