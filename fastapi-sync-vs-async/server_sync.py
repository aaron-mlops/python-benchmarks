import time
import uvicorn
from fastapi import FastAPI

app = FastAPI(docs_url="/swagger")


@app.get("/sleep")
def api_test():
    time.sleep(1)
    return 1


if __name__ == "__main__":
    uvicorn.run("server_sync:app", host="0.0.0.0", port=8002, workers=1)
