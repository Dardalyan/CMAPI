from fastapi import Request, APIRouter
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from starlette.responses import JSONResponse
from app_config.config import settings


class MailController:

    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route(settings.mail_url, self.send_mail, methods=["POST"])

        self.SMTP_SERVER = settings.smtp_server
        self.SMTP_PORT = int(settings.smtp_port)
        self.SENDER_EMAIL = settings.mail_sender_username
        self.SENDER_PASSWORD = settings.mail_sender_password

    async def send_mail(self, request: Request):
        """
        Sends an email to the target address specified in the settings, using the JSON body from the provided request object.

        The JSON body must contain the necessary information which are 'subject' and 'message'.
        """

        body = await request.json()

        subject = body.get("subject")
        message = body.get("message")

        target = settings.mail_target

        s = subject
        m = message

        # Mail Content Creation
        msg = MIMEMultipart()  # MIMEMultipart : to send multiple e-mail content
        msg["From"] = self.SENDER_EMAIL
        msg["To"] = target
        msg["Subject"] = s
        msg.attach(MIMEText(m, "plain"))  # MIMEText : to send only text content

        try:
            server = smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT)
            server.starttls()
            server.login(self.SENDER_EMAIL, self.SENDER_PASSWORD)
            server.sendmail(self.SENDER_EMAIL, target, msg.as_string())
            server.quit()

            return JSONResponse(
                status_code=200,
                content={"message": "Mail has been sent."}
            )

        except Exception as e:

            print(e)

            return JSONResponse(
                status_code=400,
                content={"message": "Mail could not be sent."}
            )
