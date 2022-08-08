import json
import requests

from appointment_mail_notifier.loggin import get_logger
from appointment_mail_notifier.notifier.mail_sender import MailSender

logger = get_logger()


class MailNotifier:
    def __init__(self, site_url: str, mail_config: dict):
        self.email_sender = MailSender(mail_config)
        self.session = requests.Session()
        self.site_url = site_url

    def handle(self):
        try:
            response = self.session.get(self.site_url)
            json_data = json.loads(response.text)
            if len(json_data) > 0:
                kwargs = {"subject": "AMN - Appointment Available"}
                self.email_sender.send(**kwargs)
                logger.info("Appointment available")
            else:
                logger.info("Appointment not available")
        except Exception as ex:
            logger.error(f"An exception has occurred with {ex}.")
