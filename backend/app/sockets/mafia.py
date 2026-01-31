import socketio

sio = socketio.AsyncServer(cors_allowed_origins="*")
sio_app = socketio.ASGIApp(sio)

@sio.event
async def connect(sid, environ):
    print("Connected:", sid)

@sio.event
async def join_game(sid, data):
    game_id = data["game_id"]
    sio.enter_room(sid, game_id)
