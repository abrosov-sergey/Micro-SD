from uuid import UUID

from email.mime.text import MIMEText
import smtplib
import ssl

from config import (
    MAIL_KEY, EMAIL_SENDER, MESSAGE_NEW_STATUS,
    SMTP_PORT, SERVER, DIC_STATUS
)


class MailSender:

    @staticmethod
    def __send_letter(email: str, message_to_send: str):
        simple_email_context = ssl.create_default_context()
        msg = MIMEText(message_to_send,'html')
        msg['Subject'] = 'Новый статус сессии'
        try:
            TIE_server = smtplib.SMTP(SERVER, SMTP_PORT)
            TIE_server.starttls(context=simple_email_context)
            TIE_server.login(EMAIL_SENDER, MAIL_KEY)
            TIE_server.sendmail(EMAIL_SENDER, email, msg.as_string())
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            TIE_server.quit()

    @staticmethod
    def send_new_status(email: str, new_status: int, session_id: UUID):
        return MailSender.__send_letter(
            email,
            MESSAGE_NEW_STATUS.format(
                session_id,
                DIC_STATUS.get(new_status) or "undefined"
            )
        )
