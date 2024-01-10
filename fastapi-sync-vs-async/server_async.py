import asyncio
import uvicorn
from fastapi import FastAPI

app = FastAPI(docs_url="/swagger")


@app.get("/sleep")
async def api_test():
    await asyncio.sleep(1)
    return 1


if __name__ == "__main__":
    uvicorn.run("server_async:app", host="0.0.0.0", port=8002, workers=1)
