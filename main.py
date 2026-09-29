from fastapi import FastAPI

app = FastAPI(title="null")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"service": "null", "owner": "null"}
