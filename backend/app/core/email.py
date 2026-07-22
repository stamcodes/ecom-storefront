import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.core.config import settings

FROM_EMAIL = settings.FROM_EMAIL


def send_email(to: str, subject: str, body: str, html: bool = False) -> None:
    msg = MIMEMultipart()
    msg["From"] = FROM_EMAIL
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html" if html else "plain"))

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.starttls()
        server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, [to], msg.as_string())


def send_verification_email(to: str, token: str) -> None:
    link = f"{settings.FRONTEND_URL}/verify-email?token={token}"
    subject = "Verify your email"
    body = f"Click the link to verify your email: {link}\nThis link expires in 24 hours."
    send_email(to, subject, body)


def send_password_reset_email(to: str, token: str) -> None:
    link = f"{settings.FRONTEND_URL}/reset-password?token={token}"
    subject = "Reset your password"
    body = f"Click the link to reset your password: {link}\nThis link expires in 1 hour."
    send_email(to, subject, body)