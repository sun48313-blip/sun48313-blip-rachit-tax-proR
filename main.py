 from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from database import get_db, create_tables

app = FastAPI(title="Rachit Tax Pro")

# ================== SESSION ==================
app.add_middleware(SessionMiddleware, secret_key="super-secret-key")

# ================== STATIC ==================
app.mount("/static", StaticFiles(directory="static"), name="static")

# ================== TEMPLATES ==================
templates = Jinja2Templates(directory="templates")

# ================== CREATE TABLES ==================
create_tables()

# ================== HOME / DASHBOARD ==================
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    user = request.session.get("user")
    if not user:
        return RedirectResponse("/login", status_code=302)

    return templates.TemplateResponse(
        "home.html",
        {"request": request, "message": "Login successful"}
    )

# ================== LOGIN PAGE ==================
@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "error": None}
    )

# ================== LOGIN POST (IMPORTANT) ==================
@app.post("/login")
def login_post(
    request: Request,
    username: str = Form(...),
    password: str = Form(...)
):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        request.session["user"] = username
        return RedirectResponse("/", status_code=302)

    return templates.TemplateResponse(
        "login.html",
        {
            "request": request,
            "error": "Invalid username or password"
        }
    )

# ================== LOGOUT ==================
@app.get("/logout")
def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/login", status_code=302)

# ================== GST ==================
@app.get("/gst", response_class=HTMLResponse)
def gst(request: Request):
    if not request.session.get("user"):
        return RedirectResponse("/login", status_code=302)

    return templates.TemplateResponse("gst.html", {"request": request})

# ================== ITR ==================
@app.get("/itr", response_class=HTMLResponse)
def itr(request: Request):
    if not request.session.get("user"):
        return RedirectResponse("/login", status_code=302)

    return templates.TemplateResponse("itr.html", {"request": request})

# ================== CLIENTS ==================
@app.get("/clients", response_class=HTMLResponse)
def clients(request: Request):
    if not request.session.get("user"):
        return RedirectResponse("/login", status_code=302)

    return templates.TemplateResponse("clients.html", {"request": request})



 
 
 

 
