from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://workana-premium.workable.com"],  # 👈 or ["*"] for any origin (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@router.get("/")
async def root():
    return {"message": "Zdravo svet! -Piton"}