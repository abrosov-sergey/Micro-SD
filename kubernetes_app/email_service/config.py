from decouple import config

MAIL_KEY = config("MAIL_KEY")
EMAIL_SENDER = config("EMAIL_SENDER")
SMTP_PORT = 587
SERVER = "smtp.gmail.com"

MESSAGE_NEW_STATUS = """
<!DOCTYPE html>
<html>
<body>
    <h2>Для вашей  сессии {0} установлен новый статус:</h2>
    <h4>{1}</h4>

</body>
</html>
"""

DIC_STATUS = {
    1: "Initial",
    2: "Ready",
    3: "Running",
    4: "Success",
    5: "Error"
}
