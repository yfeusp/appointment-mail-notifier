from appointment_mail_notifier import config
from appointment_mail_notifier.notifier.daily_notifier import DailyNotifier
from appointment_mail_notifier.loggin import get_logger
from appointment_mail_notifier.notifier.mail_notifier import MailNotifier

logger = get_logger()
mail_notifier = MailNotifier(config.site_url, config.email)
daily_notifier = DailyNotifier(config.email)


def run_notifiers():
    try:
        mail_notifier.start()
        daily_notifier.start()
    except Exception as ex:
        logger.error(f"An exception has occurred with {ex}.")


def main():
    run_notifiers()


if __name__ == "__main__":
    main()
