from fastapi import FastAPI, HTTPException

from mail import MailSender
from schemas import NewStatusSchema


app = FastAPI()


@app.post("/session/notify")
def send_notification(change_status: NewStatusSchema):
    if not MailSender.send_new_status(
        new_status=change_status.new_status_id,
        email=change_status.email,
        session_id=change_status.session_id,
    ):
        raise HTTPException(
            detail="Notification could not be sended",
            status_code=422,
        )



# import uvicorn
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8084)
