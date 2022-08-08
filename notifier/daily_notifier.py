from datetime import datetime

from notifier.loggin import get_logger
from notifier.mail_sender import MailSender

logger = get_logger()


class DailyNotifier:
    def __init__(self, mail_config: dict):
        self.email_sender = MailSender(mail_config)
        self.days = []

    def handle(self):
        try:
            now_srt = datetime.now().strftime("%d-%m-%Y")
            if now_srt not in self.days:
                kwargs = {"subject": "AMN - Daily Notification"}
                self.email_sender.send(**kwargs)
                self.days.append(now_srt)
                logger.info("Daily Notification")
        except Exception as ex:
            logger.error(f"An exception has occurred with {ex}.")
