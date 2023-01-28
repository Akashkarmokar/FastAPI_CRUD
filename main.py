from fastapi import  FastAPI


app = FastAPI()


@app.get('/index')
async def index():
    return { 'status': 'OK', 'msg': "Data fetched successfully"}