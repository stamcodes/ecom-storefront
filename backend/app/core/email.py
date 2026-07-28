import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.core.config import settings

import logging

logger = logging.getLogger(__name__)


def send_email(to: str, subject: str, body: str, html: bool = False) -> bool:
    if not settings.SMTP_USERNAME or not settings.SMTP_PASSWORD:
        logger.warning("SMTP_USERNAME or SMTP_PASSWORD not set in environment. Skipping email dispatch.")
        print(f"[EMAIL MOCK] To: {to} | Subject: {subject} | Body: {body}")
        return False

    msg = MIMEMultipart()
    msg["From"] = settings.FROM_EMAIL
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html" if html else "plain"))

    try:
        if settings.SMTP_PORT == 465:
            with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT, timeout=10) as server:
                server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
                server.sendmail(settings.FROM_EMAIL, [to], msg.as_string())
        else:
            with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT, timeout=10) as server:
                server.starttls()
                server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
                server.sendmail(settings.FROM_EMAIL, [to], msg.as_string())
        logger.info(f"Email successfully sent to {to}")
        print(f"[EMAIL SENT] Successfully sent email to {to}")
        return True
    except Exception as e:
        logger.error(f"Failed to send email to {to} via {settings.SMTP_HOST}:{settings.SMTP_PORT}: {e}")
        print(f"[EMAIL ERROR] Failed to send email to {to}: {e}")
        return False


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