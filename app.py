from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_location():
    return {
        "location": "Classroom",
        "latitude": 9.9332,
        "longitude": 78.1200
    }