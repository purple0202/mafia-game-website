from fastapi import FastAPI
from app.auth.routes import router as auth_router
from app.games.routes import router as game_router
from app.sockets.mafia import sio_app

app = FastAPI(title="Mafia Game API")

app.include_router(auth_router, prefix="/auth")
app.include_router(game_router, prefix="/games")

# Mount Socket.IO
app.mount("/ws", sio_app)
