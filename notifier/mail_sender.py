import smtplib
from socket import gaierror
from email.message import EmailMessage

from notifier.exceptions import (
    InvalidRecipientError,
    HostOrPortFailedConnectionError,
    InvalidMailCredentialsError,
)
from notifier.loggin import get_logger

logger = get_logger()


class MailSender:
    def __init__(self, mail_config: dict):
        self.email_message = EmailMessage()
        self.mail_config = mail_config

    def send(self, **kwargs):
        self.email_message["Subject"] = kwargs.get("subject")
        self.email_message["From"] = self.mail_config["smtp_username"]
        self.email_message["To"] = self.mail_config["email_recipient"]
        logged_in_smtp = self.__login_smtp()
        self.__send_smtp_message(logged_in_smtp)
        logged_in_smtp.quit()

    def __send_smtp_message(self, logged_in_smtp):
        try:
            if logged_in_smtp:
                logged_in_smtp.send_message(self.email_message)
        except Exception as ex:
            if isinstance(ex, smtplib.SMTPRecipientsRefused):
                raise InvalidRecipientError()
            logger.error(f"An exception has occurred with {ex}.")

    def __login_smtp(self):
        try:
            logged_in_smtp = smtplib.SMTP_SSL(
                self.mail_config["smtp_host"], self.mail_config["smtp_port"]
            )

            logged_in_smtp.login(
                self.mail_config["smtp_username"], self.mail_config["smtp_password"]
            )
            return logged_in_smtp
        except Exception as ex:
            if isinstance(ex, gaierror):
                logger.error(
                    "Server could not be connected to mail host or port."
                )
                raise HostOrPortFailedConnectionError()
            if isinstance(ex, smtplib.SMTPAuthenticationError):
                raise InvalidMailCredentialsError()
            logger.error(f"An exception has occurred with {ex}.")
