from fastapi import FastAPI, HTTPException, Path, Body
from pydantic import BaseModel
from typing import Optional, Dict
from enum import Enum 

app = FastAPI(
    title="mETaL - OpenAPI 3.0",
    description="This is one of mETaL's microservices based on the OpenAPI 3.0 specification.",
    version="1.0.0"
)

# Models for request and response schemas
class SessionStatus(str, Enum):
    INITIAL = "Initial"
    READY = "Ready"
    RUNNING = "Running"
    SUCCESS = "Success"
    ERROR = "Error"

class SessionCreateRequest(BaseModel):
    configId: str
    processingParameters: Optional[Dict[str, str]] = None

class Session(BaseModel):
    sessionId: str
    config: str
    processingParameters: Optional[Dict[str, str]]
    status: SessionStatus

class SessionStatusUpdate(BaseModel):
    status: SessionStatus


# In-memory database mockup for demonstration
sessions = {}


# Endpoints
@app.post("/sessions", response_model=Session, status_code=201)
async def create_session(request: SessionCreateRequest = Body(...)):
    """Create a new session."""
    new_session_id = f"session_{len(sessions) + 1}"
    session = Session(
        sessionId=new_session_id,
        config=request.configId,
        processingParameters=request.processingParameters,
        status=SessionStatus.INITIAL
    )
    sessions[new_session_id] = session
    return session


@app.get("/sessions/{sessionId}", response_model=Session)
async def get_session(sessionId: str = Path(..., description="Unique session ID")):
    """Get session details by ID."""
    session = sessions.get(sessionId)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session


@app.delete("/sessions/{sessionId}", status_code=204)
async def delete_session(sessionId: str = Path(..., description="Unique session ID")):
    """Delete a session by ID."""
    if sessionId not in sessions:
        raise HTTPException(status_code=404, detail="Session not found")
    del sessions[sessionId]
    return


@app.get("/sessions/{sessionId}/status", response_model=SessionStatus)
async def get_session_status(sessionId: str = Path(..., description="Unique session ID")):
    """Get the status of a session."""
    session = sessions.get(sessionId)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return session.status


@app.put("/sessions/{sessionId}/status", response_model=SessionStatus)
async def update_session_status(
    sessionId: str = Path(..., description="Unique session ID"),
    status_update: SessionStatusUpdate = Body(...)
):
    """Update the status of a session."""
    session = sessions.get(sessionId)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    session.status = status_update.status
    return session.status