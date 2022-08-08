import time

from appointment_mail_notifier import config
from appointment_mail_notifier.config import waiting_time
from appointment_mail_notifier.notifier.daily_notifier import DailyNotifier
from appointment_mail_notifier.loggin import get_logger
from appointment_mail_notifier.notifier.mail_notifier import MailNotifier

logger = get_logger()
mail_notifier = MailNotifier(config.site_url, config.email)
daily_notifier = DailyNotifier(config.email)


def run_notifiers(number_of_iterations=-1):
    try:
        while number_of_iterations != 0:
            # Appointment appointment_mail_notifier
            mail_notifier.handle()
            # Daily appointment_mail_notifier
            daily_notifier.handle()
            # Wait
            time.sleep(waiting_time)
            number_of_iterations -= 1
    except Exception as ex:
        logger.error(f"An exception has occurred with {ex}.")


def main():
    run_notifiers()


if __name__ == "__main__":
    main()
