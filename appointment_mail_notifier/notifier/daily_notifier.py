import time
from datetime import datetime

from appointment_mail_notifier.config import waiting_time
from appointment_mail_notifier.loggin import get_logger
from appointment_mail_notifier.notifier.mail_sender import MailSender

logger = get_logger()


class DailyNotifier:
    def __init__(self, mail_config: dict):
        self.email_sender = MailSender(mail_config)
        self.days = []

    def start(self, number_of_iterations=-1):
        try:
            while number_of_iterations != 0:
                now_srt = datetime.now().strftime("%d-%m-%Y")
                if now_srt not in self.days:
                    kwargs = {"subject": "AMN - Daily Notification"}
                    self.email_sender.send(**kwargs)
                    self.days.append(now_srt)
                    logger.info("Daily Notification")
                number_of_iterations -= 1
                time.sleep(waiting_time)
        except Exception as ex:
            logger.error(f"An exception has occurred with {ex}.")
