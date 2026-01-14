from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Rachit Tax Pro")

# static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# templates
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/gst", response_class=HTMLResponse)
def gst(request: Request):
    return templates.TemplateResponse("gst.html", {"request": request})


@app.get("/itr", response_class=HTMLResponse)
def itr(request: Request):
    return templates.TemplateResponse("itr.html", {"request": request})


@app.get("/clients", response_class=HTMLResponse)
def clients(request: Request):
    return templates.TemplateResponse("clients.html", {"request": request})

 
 
 

 
