from fastapi import FastAPI

app = FastAPI(title="GitHub Actions Demo")


@app.get("/hello")
def hello():
    return {"message": "Hello, GitHub!"}