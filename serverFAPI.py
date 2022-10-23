from fastapi import FastAPI,UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from glob import glob
from starlette.responses import FileResponse
fileContent={}
fileContent["index.html"]=open("templates/index.html","r",encoding="utf-8").read()
app=FastAPI()
app.mount("/static",StaticFiles(directory="static"),name="static")
@app.get("/")
async def index():
    return HTMLResponse(content=fileContent["index.html"],status_code=200)
@app.get("/download/100mb")
async def download100mb():
    return FileResponse("D:\\NetSpeedSampleFiles\\100mb.zip", media_type='application/octet-stream',filename="100mb.zip")
@app.get("/download/50mb")
async def download100mb():
    return FileResponse("D:\\NetSpeedSampleFiles\\50mb.zip", media_type='application/octet-stream',filename="100mb.zip")
@app.post("/upload")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
@app.get("/emptyData")
async def emptyData():
    return ""