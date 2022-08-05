import os
from dotenv import load_dotenv

load_dotenv()

email = {
    "smtp_host": os.environ.get("SMTP_HOST"),
    "smtp_port": os.environ.get("SMTP_PORT"),
    "smtp_username": os.environ.get("SMTP_USERNAME"),
    "smtp_password": os.environ.get("SMTP_PASSWORD"),
    "email_recipient": os.environ.get("EMAIL_RECIPIENT"),
    "email_subject": os.environ.get("EMAIL_SUBJECT"),
}

log_config = {
    "log_level": os.environ.get("LOG_LEVEL", "INFO"),
    "log_name": os.environ.get("LOG_NAME", "AMN"),
    "log_format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
}
