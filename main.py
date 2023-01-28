from fastapi import  FastAPI
import uvicorn

app = FastAPI()


@app.get('/index')
async def index():
    return { 'status': 'OK', 'msg': "Data fetched successfully"}




if __name__ == "__main__":
    uvicorn.run(app=app)