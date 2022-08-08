import time

from notifier import config
from notifier.config import waiting_time
from notifier.daily_notifier import DailyNotifier
from notifier.loggin import get_logger
from notifier.mail_notifier import MailNotifier

logger = get_logger()
mail_notifier = MailNotifier(config.site_url, config.email)
daily_notifier = DailyNotifier(config.email)


def main(number_of_iterations=-1):
    try:
        while number_of_iterations != 0:
            # Appointment notifier
            mail_notifier.handle()
            # Daily notifier
            daily_notifier.handle()
            # Wait
            time.sleep(waiting_time)
            number_of_iterations -= 1
    except Exception as ex:
        logger.error(f"An exception has occurred with {ex}.")


if __name__ == "__main__":
    main()
