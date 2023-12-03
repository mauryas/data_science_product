from fastapi import FastAPI

from app.distance import router as distance_app
from app.trees import router as tree_app

app = FastAPI()

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "message": "Welcome to api for tasks. \
            Please execute the refers to the url/docs for end points"
    }


app.include_router(distance_app, tags=["distance"])
app.include_router(tree_app, tags=["decisiontree"])
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888)
