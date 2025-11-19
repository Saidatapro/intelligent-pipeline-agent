
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
router = APIRouter(tags=["ws"])
@router.websocket("/ws/pipelines/{pid}")
async def ws_pipeline(ws: WebSocket, pid: int):
    await ws.accept()
    try:
        await ws.send_text(f"Subscribed {pid}")
        while True:
            msg = await ws.receive_text()
            await ws.send_text("echo:"+msg)
    except WebSocketDisconnect:
        pass
