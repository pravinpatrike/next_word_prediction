import uvicorn

def main():
    # Programmatically run FastAPI using uvicorn
    uvicorn.run("src.api:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()
