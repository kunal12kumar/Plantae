from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import disease

app = FastAPI()
app.include_router(disease.router)

# Enable if testing from browser form
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # OR use your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
