from fastapi import FastAPI

app = FastAPI(
    title="Helmet Violation Detection Platform"
)

@app.get("/")
def root():
    return {"message": "Application Running"}