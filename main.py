from fastapi import FastAPI
from database import init_db
from routes import auth, nfe, dashboard

app = FastAPI()

init_db()

app.include_router(auth.router)
app.include_router(nfe.router)
app.include_router(dashboard.router)
